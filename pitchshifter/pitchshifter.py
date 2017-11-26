#!python
##
# pitch-shifter-cli.py: Pitch Shifter Command Line Tool
# 
# Author(s): Chris Woodall <chris@cwoodall.com>
# BSD License 2015 (c) Chris Woodall <chris@cwoodal.com>
##
import argparse
import matplotlib.pyplot as pp
import numpy as np
import scipy
import scipy.interpolate
import scipy.io.wavfile
import sys
import logging
from . import *

logging.basicConfig(filename='pitchshifter-cli.log', filemode='w', level=logging.DEBUG)


def main(args={}):
    # Try to open the wav file and read it
    try:
        source = scipy.io.wavfile.read(args.source)
    except:
        print("File {0} does not exist".format(args.source))
        sys.exit(-1)

    RESAMPLING_FACTOR = 2**(args.pitch/12)
    HOP = int((1-args.overlap)*args.chunk_size)
    HOP_OUT = int(HOP*RESAMPLING_FACTOR)
    
    audio_samples = source[1].tolist()

    rate = source[0]
    mono_samples = stereoToMono(audio_samples)
    frames = stft(mono_samples, args.chunk_size, HOP)
    vocoder = PhaseVocoder(HOP, HOP_OUT)
    adjusted = [frame for frame in vocoder.sendFrames(frames)]

    merged_together = istft(adjusted, args.chunk_size, HOP_OUT)

    if args.no_resample:
        final = merged_together
    else:
        resampled = linear_resample(merged_together, 
                                       len(mono_samples))
        final = resampled * args.blend + (1-args.blend) * mono_samples

    if args.debug:
        pp.plot(final)
        pp.show()
    
    output = scipy.io.wavfile.write(args.out, rate, np.asarray(final, dtype=np.int16))
    

def cli():
    parser = argparse.ArgumentParser(
        description = "Shifts the pitch of an input .wav file")
    parser.add_argument('--source', '-s', help='source .wav file', required=True)
    parser.add_argument('--out', '-o', help='output .wav file', required=True)
    parser.add_argument('--pitch', '-p', help='pitch shift', default=0, type=float)
    parser.add_argument('--blend', '-b', help='blend', default=1, type=float)
    parser.add_argument('--chunk-size', '-c', help='chunk size', default=4096, type=int)
    parser.add_argument('--overlap', '-e', help='overlap', default=.9, type=float)
    parser.add_argument('--debug', '-d', help='debug flag', action="store_true")
    parser.add_argument('--no-resample', help='debug flag', action="store_true")  

    args = parser.parse_args()
    main(args)

if __name__ == "__main__":
    cli()