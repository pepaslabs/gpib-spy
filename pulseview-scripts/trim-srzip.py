#!/usr/bin/env python

# trim-srzip.py: trim the leading and trailing steady-state from an srzip.
# Copyright Jason Pepas, 2017.  Released under the terms of the MIT License.
# See https://opensource.org/licenses/MIT

import sys
import os
import zipfile
import zlib
import tempfile
import ConfigParser
import shutil

if len(sys.argv) < 2:
    sys.stderr.write("trim-srzip.py: trim the leading and trailing steady-state from an srzip.\n")
    sys.stderr.write("Usage: trim-srzip.py <srzip> [<pad>]\n")
    sys.stderr.write("e.g.: ./trim-srzip.py foo.sr 100\n")
    sys.exit(1)

fname = sys.argv[1]

orig_fname = fname + ".orig"
assert os.path.exists(orig_fname) == False
shutil.move(fname, orig_fname)

# by default, keep a 10-sample pad of steady-state samples (leading and trailing)
pad = 10

if len(sys.argv) > 2:
    pad = sys.argv[2]

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

unitsize = None
# Read the unitsize from the metadata file
with zin.open("metadata", 'r') as fin:
    metadata = ConfigParser.ConfigParser()
    metadata.readfp(fin)
    unitsize = int(metadata.get('device 1', 'unitsize'))

# Trim the sample file
with zin.open("logic-1-1", 'r') as f:
    with tempfile.NamedTemporaryFile() as f_out:
        samples = f.read()
        assert len(samples) >= unitsize

        # start at the first sample and look for the first change.        
        start_index = 0
        first_sample = samples[start_index: start_index + unitsize]
        while start_index < len(samples):
            this_sample = samples[start_index: start_index + unitsize]
            if this_sample != first_sample:
                # This is the first change.  Back up one sample.
                start_index -= unitsize
                break
            else:
                start_index += unitsize
                continue
        assert start_index != len(samples)

        start_index -= pad * unitsize
        if start_index < 0:
            start_index = 0

        # start at the last sample and work our way backwards, looking for a change.
        end_index = len(samples) - unitsize
        last_sample = samples[end_index: end_index + unitsize]
        while end_index >= 0:
            this_sample = samples[end_index: end_index + unitsize]
            if this_sample != last_sample:
                # This is the first change.  Back up one sample.
                end_index += unitsize
                break
            else:
                end_index -= unitsize
                continue
        assert end_index >= 0

        end_index += pad
        if end_index > (len(samples) - unitsize):
            end_index = len(samples) - unitsize

        assert start_index < end_index

        samples = samples[start_index:end_index]

        f_out.write(samples)
        f_out.flush()
        zout.write(f_out.name, "logic-1-1")

zin.close()
zout.close()

os.unlink(orig_fname)
