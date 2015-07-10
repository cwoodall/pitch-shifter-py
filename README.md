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

This will install pitch-shifter.py

## Requirements

Please see setup.py and requirements.txt files. No additional requirements need to be satisfied.

# Example Usage

The following command 
```
$ export PYTHONPATH=.
$ python ./bin/pitch-shifter.py -s ./samples/sample1.wav -o out.wav -c 4096 -e .9 -p -7 -b .8
$ totem out.wav
```
# References

1. [Guitar Pitch Shifter][grodin1] by François Grondin
2. [Phase Vocoder Tutorial][dolson1] by Mark Dolson
3. [NEW PHASE-VOCODER TECHNIQUES FOR PITCH-SHIFTING, HARMONIZING AND OTHER EXOTIC EFFECTS][laroche1] by Laroche and Dolson
4. [Phase-Vocoder: About this phasing business][laroche2] by Laroche and Dolson
5. [Phase Locked Vocoder][puckette1] by Puckette
6. [Improved Phase Vocoder Time-Scale Modification of Audio][laroche3] by Laroche and Dolson

[grodin1]: http://www.guitarpitchshifter.com
[dolson1]: http://www.eumus.edu.uy/eme/ensenanza/electivas/dsp/presentaciones/PhaseVocoderTutorial.pdf
[laroche1]: http://labrosa.ee.columbia.edu/~dpwe/papers/LaroD99-pvoc.pdf
[laroche2]: http://www.ee.columbia.edu/~dpwe/papers/LaroD97-phasiness.pdf
[puckette1]: http://msp.ucsd.edu/Publications/mohonk95.pdf
[laroche3]: http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCQQFjAAahUKEwj-gI_gp9HGAhWKPZIKHafnDTM&url=http%3A%2F%2Fwww.cmap.polytechnique.fr%2F~bacry%2FMVA%2Fgetpapers.php%3Ffile%3Dphase_vocoder.pdf%26type%3Dpdf&ei=qx6gVb7_O4r7yASnz7eYAw&usg=AFQjCNFywrNRdVKK9ZhRpQoRjtn5kP4p_A&sig2=wM7GAqHftEI0yB5z4y5i7w&bvm=bv.97653015,d.aWw
