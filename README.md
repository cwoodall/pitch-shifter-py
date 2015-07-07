Shifts the pitch of an input wav file...


Examples coming
# Basic Algorithm Flow

```
Input --> Phase Vocoder (Stretch or compress by 2^(n/12)) --> resample by 2^(n/12)
```

# Installing

Uses python2.7. Only tested on Linux (Ubuntu 14.04)

```
$ python setup.py install
```

# Example Usage

The following command 
```
$ export PYTHONPATH=.
$ python ./bin/pitch-shifter.py -s ./samples/sample1.wav -o out.wav -c 4096 -e .9 -p -7 -b .8
$ totem out.wav
```
# References

1. [Guitar Pitch Shifter][1] by François Grondin
2. [Phase Vocoder Tutorial][2]

[1]: http://www.guitarpitchshifter.com
[2]: http://www.eumus.edu.uy/eme/ensenanza/electivas/dsp/presentaciones/PhaseVocoderTutorial.pdf
