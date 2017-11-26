#!python
##
# pitch-shifter-cli.py: Pitch Shifter Command Line Tool
# 
# Author(s): Chris Woodall <chris@cwoodall.com>
# BSD License 2015 (c) Chris Woodall <chris@cwoodal.com>
##
import matplotlib.pyplot as pp
import numpy as np
import scipy
import scipy.interpolate
import scipy.io.wavfile
import sys
import logging
from . import *
import click

logging.basicConfig(filename='pitchshifter-cli.log', filemode='w', level=logging.DEBUG)

@click.command()
@click.argument("source")
@click.option("--out", "-o", default="out.wav", type=str, help="output .wav file")
@click.option("--pitch", "-p", help="Pitch shift in terms of semitones", default = 0, type=float)
@click.option("--blend", "-b", help="Blend the input and output (disabled in no-resample mode). 0 to 1", default = 1, type=float)
@click.option('--chunk-size', '-c', help='chunk size', default=4096, type=int)
@click.option('--overlap', '-e', help='overlap', default=.9, type=float)
@click.option('--debug/--no-debug', default=False)
@click.option('--resample/--no-resample', default=True)
def cli(source, out, pitch, blend, chunk_size, overlap, debug, resample):
    # Try to open the wav file and read it
    try:
        source = scipy.io.wavfile.read(source)
    except:
        print("File {0} does not exist".format(source))
        sys.exit(-1)

    RESAMPLING_FACTOR = 2**(pitch/12)
    HOP = int((1-overlap)*chunk_size)
    HOP_OUT = int(HOP*RESAMPLING_FACTOR)
    
    audio_samples = source[1].tolist()

    rate = source[0]
    mono_samples = stereoToMono(audio_samples)
    frames = stft(mono_samples, chunk_size, HOP)
    vocoder = PhaseVocoder(HOP, HOP_OUT)
    adjusted = [frame for frame in vocoder.sendFrames(frames)]

    merged_together = istft(adjusted, chunk_size, HOP_OUT)

    if resample:
        resampled = linear_resample(merged_together, 
                                    len(mono_samples))
        final = resampled * blend + (1-blend) * mono_samples
    else:
        final = merged_together

    if debug:
        pp.plot(final)
        pp.show()
    
    output = scipy.io.wavfile.write(out, rate, np.asarray(final, dtype=np.int16))

if __name__ == "__main__":
    cli()