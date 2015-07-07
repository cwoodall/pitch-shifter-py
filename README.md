Shifts the pitch of an input wav file...


Examples coming
# Basic Algorithm Flow

```
Input --> Phase Vocoder (Stretch or compress by 2^(n/12)) --> resample by 2^(n/12)
```

# Example command
> python ./pitch-shifter.py -s ./gtr-jazz-3.wav -o wow.wav -c 4096 -e .9 -p -7 -b .8; totem wow.wav

# References

1. [Guitar Pitch Shifter][1] by François Grondin
2. [Phase Vocoder Tutorial][2]

[1]: http://www.guitarpitchshifter.com
[2]: http://www.eumus.edu.uy/eme/ensenanza/electivas/dsp/presentaciones/PhaseVocoderTutorial.pdf)
