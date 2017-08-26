This is a series of scripts for manipulating the 'srzip' data files
captured by Pulseview (the open-source logic analyzer GUI).

In particular, this set of scripts was written to allow using two
8-channel logic analyzers together to analyze the 16-channel GPIB
bus.

Capturing data using two devices simultaneously requires a patch
to Pulseview, see the attachment on this message:
https://sourceforge.net/p/sigrok/mailman/message/35958181/

After capturing data using two 8-channel analyzers (with output
files named "control.sr" and "data.sr"), run the scripts like so:

./mux-2x8ch.py control.sr data.sr muxed.sr
./align-2x8ch-gpib.py muxed.sr
./trim-srzip.py muxed.sr
./gpib-pin-namer.py muxed.sr

Note that mux-2x8ch.py takes quite a long time to run (~30 seconds
for 5M samples).
