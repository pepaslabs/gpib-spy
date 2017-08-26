#!/usr/bin/env python

# mux2x8ch.py: mux two 8-channel srzip files into one 16-channel file.
# Copyright Jason Pepas, 2017.  Released under the terms of the MIT License.
# See https://opensource.org/licenses/MIT

import sys
import os
import zipfile
import zlib
import tempfile
import ConfigParser

if len(sys.argv) < 4:
    sys.stderr.write("mux2x8ch.py: mux two 8-channel srzip files into a single 16-channel file.\n")
    sys.stderr.write("Usage: mux2x8ch.py <input A> <input B> <output>\n")
    sys.stderr.write("e.g.: ./mux2x8ch.py A.sr B.sr out.sr\n")
    sys.exit(1)

input_fname_A = sys.argv[1]
input_fname_B = sys.argv[2]
out_fname = sys.argv[3]

zin_A = zipfile.ZipFile(input_fname_A, 'r')
zin_B = zipfile.ZipFile(input_fname_B, 'r')
zout = zipfile.ZipFile(out_fname, mode='w', compression=zipfile.ZIP_DEFLATED)

# Check that the two 'version' files match, then copy one to the output
with zin_A.open("version", 'r') as f_A:
    with zin_B.open("version", 'r') as f_B:
        with tempfile.NamedTemporaryFile() as f_out:
            version_A = f_A.read()
            version_B = f_B.read()
            assert version_A == version_B
            f_out.write(version_A)
            f_out.flush()
            zout.write(f_out.name, "version")

# Merge the two 'metadata' files as best we can
with zin_A.open("metadata", 'r') as f_A:
    with zin_B.open("metadata", 'r') as f_B:
        with tempfile.NamedTemporaryFile() as f_out:
            metadata_A = ConfigParser.ConfigParser()
            metadata_A.readfp(f_A)
            metadata_B = ConfigParser.ConfigParser()
            metadata_B.readfp(f_B)
            metadata_A.set('device 1', 'total probes', 16)
            metadata_A.set('device 1', 'unitsize', 2)
            metadata_A.set('device 1', 'probe9', metadata_B.get('device 1', 'probe1'))
            metadata_A.set('device 1', 'probe10', metadata_B.get('device 1', 'probe2'))
            metadata_A.set('device 1', 'probe11', metadata_B.get('device 1', 'probe3'))
            metadata_A.set('device 1', 'probe12', metadata_B.get('device 1', 'probe4'))
            metadata_A.set('device 1', 'probe13', metadata_B.get('device 1', 'probe5'))
            metadata_A.set('device 1', 'probe14', metadata_B.get('device 1', 'probe6'))
            metadata_A.set('device 1', 'probe15', metadata_B.get('device 1', 'probe7'))
            metadata_A.set('device 1', 'probe16', metadata_B.get('device 1', 'probe8'))
            metadata_A.write(f_out)
            f_out.flush()
            zout.write(f_out.name, "metadata")

# Mux the two sample files
with zin_A.open("logic-1-1", 'r') as f_A:
    with zin_B.open("logic-1-1", 'r') as f_B:
        with tempfile.NamedTemporaryFile() as f_out:
            while True:
                sample_A = f_A.read(1)
                sample_B = f_B.read(1)
                if len(sample_A) == 0 or len(sample_B) == 0:
                    break
                f_out.write(sample_A)
                f_out.write(sample_B)
            f_out.flush()
            zout.write(f_out.name, "logic-1-1")

zin_A.close()
zin_B.close()
zout.close()

