#!/usr/bin/env python

# align-2x8ch-gpib.py: automatically align two 8-channel GPIB analyzers.
# Copyright Jason Pepas, 2017.  Released under the terms of the MIT License.

# Strategy: look for the first sample where DAV goes low.  The first change to
# any data line should happen just before DAV goes low.

# Note: the GPIB control lines are assumed to be probes 1-8, and the data
# lines are assumed to be 9-16.  DAV is assumed to be probe 1.

dav_pin_index = 0  # The (0-based) probe number of the DAV line


import sys
import os
import zipfile
import zlib
import tempfile
import ConfigParser
import shutil

if len(sys.argv) < 2:
    sys.stderr.write("align-2x8ch-gpib.py: automatically align two 8-channel GPIB analyzers.\n")
    sys.stderr.write("Usage: align-2x8ch-gpib.py <input>\n")
    sys.stderr.write("e.g.: ./align-2x8ch-gpib.py samples.sr\n")
    sys.exit(1)

fname = sys.argv[1]

orig_fname = fname + ".orig"
assert os.path.exists(orig_fname) == False
shutil.move(fname, orig_fname)

zin = zipfile.ZipFile(orig_fname, 'r')
zout = zipfile.ZipFile(fname, mode='w', compression=zipfile.ZIP_DEFLATED)

# Copy the 'version' file
with zin.open("version", 'r') as fin:
    with tempfile.NamedTemporaryFile() as fout:
        fout.write(fin.read())
        fout.flush()
        zout.write(fout.name, "version")

# Copy the 'metadata' file
with zin.open("metadata", 'r') as fin:
    with tempfile.NamedTemporaryFile() as fout:
        fout.write(fin.read())
        fout.flush()
        zout.write(fout.name, "metadata")

# Mux the two sample files
with zin.open("logic-1-1", 'r') as f:
    with tempfile.NamedTemporaryFile() as f_out:
        # - Seek the control lines until DAV goes low, then back off by one sample.
        # - Seek the data lines until any line changes.
        # - Write out the samples until one bank runs out.

        control_bytes = []
        data_bytes =[]

        # Read the control and data line bytes into RAM
        while True:
            control_lines = f.read(1)
            if len(control_lines) == 0:
                break
            data_lines = f.read(1)
            if len(control_lines) == 0:
                break
            control_bytes.append(control_lines)
            data_bytes.append(data_lines)

        control_bytes_len = len(control_bytes)
        data_bytes_len = len(data_bytes)

        # Find the sample just before DAV went low for the first time
        i = 0
        while i < control_bytes_len:
            control_lines = control_bytes[i]
            dav = ord(control_lines) & 1 << dav_pin_index

            # Note: GPIB is active-low, so 0 means that DAV is asserted.
            if dav == 0:
                assert i != 0
                dav_start = i - 1
                break
            else:
                i += 1
                continue

        # Find the first sample where the control lines change
        i = 0
        while i < control_bytes_len:
            control_lines = control_bytes[i]
            if control_lines != control_bytes[0]:
                control_start = i
                break
            else:
                i += 1
                continue

        # Find the first sample where the data lines change
        i = 0
        while i < data_bytes_len:
            data_lines = data_bytes[i]
            if data_lines != data_bytes[0]:
                data_start = i
                break
            else:
                i += 1
                continue

        # If dav_start comes after control_start, account for that
        if control_start < dav_start:
            delta = dav_start - control_start
            data_start -= delta

        # Add a bit of padding if possible
        if control_start > 10 and data_start > 10:
            control_start -= 10
            data_start -= 10

        # Write out the control and data lines, starting from the above offsets
        i = 0
        while control_start + i < control_bytes_len and data_start + i < data_bytes_len:
            control_lines = control_bytes[control_start + i]
            data_lines = data_bytes[data_start + i]
            f_out.write(control_lines)
            f_out.write(data_lines)
            i += 1
        
        f_out.flush()
        zout.write(f_out.name, "logic-1-1")

zin.close()
zout.close()

os.unlink(orig_fname)
