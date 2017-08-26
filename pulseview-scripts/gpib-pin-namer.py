#!/usr/bin/env python

# gpib-pin-namer.py: rename the probes of an srzip file, according to gpib-spy pin ordering.
# See https://github.com/pepaslabs/gpib-spy
# Written by Jason Pepas, 2017.  Released under the terms of the MIT License.
# See https://opensource.org/licenses/MIT

import sys
import os
import zipfile
import zlib
import tempfile
import ConfigParser
import shutil

# adjust as needed!
pinmap = {
    "DAV": "probe1",
    "NRFD": "probe2",
    "NDAC": "probe3",
    "IFC": "probe4",
    "ATN": "probe5",
    "SRQ": "probe6",
    "REN": "probe7",
    "EOI": "probe8",
    "DIO1": "probe9",
    "DIO2": "probe10",
    "DIO3": "probe11",
    "DIO4": "probe12",
    "DIO5": "probe13",
    "DIO6": "probe14",
    "DIO7": "probe15",
    "DIO8": "probe16"
}

if len(sys.argv) < 2:
    sys.stderr.write("gpib-pin-renamer.py: rename the probes of an srzip file.\n")
    sys.stderr.write("Usage: gpib-pin-renamer.py <srzip filename>\n")
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

# Copy the 'logic-1-1' file
with zin.open("logic-1-1", 'r') as fin:
    with tempfile.NamedTemporaryFile() as fout:
        fout.write(fin.read())
        fout.flush()
        zout.write(fout.name, "logic-1-1")

# Copy the 'metadata' file, renaming the probes.
with zin.open("metadata", 'r') as fin:
    with tempfile.NamedTemporaryFile() as fout:
        metadata = ConfigParser.ConfigParser()
        metadata.readfp(fin)
        for (pin_name, probe) in pinmap.iteritems():
            metadata.set('device 1', probe, pin_name)
        metadata.write(fout)
        fout.flush()
        zout.write(fout.name, "metadata")

zin.close()
zout.close()

os.unlink(orig_fname)
