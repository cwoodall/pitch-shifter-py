# Python Pitch Shifter
> Take an input .wav file and shift the pitch without
> changing the speed or length of the input file.

## Install

Require: Python 2.7 

```
$ git clone https://github.com/cwoodall/pitch-shifter-py.git
$ cd pitch-shifter-py
$ pip install .
```

For development `virtualenv` is recommended:

```
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install .
```

On systems where specific versions of `scipy` and `numpy` might be needed, those should be installed seperately (using `conda` or other means)

## Usage

The following command will shift the tone up an octave (`12` semitones) and blend it so that both have equal volume (`.5`)

```
$ pitch-shifter.py -s ./samples/sample1.wav -o out.wav -p 12 -b .5
```

This example shifts up a fifth (`7` semitones) and blends it so it is all the new shifted version:

```
$ pitch-shifter.py -s ./samples/sample1.wav -o out.wav -p 7 -b 1
```

With some tweaking you can also use this script to slow down and speed up music using the `--no-resample` switch. To
double the speed shift up and octave (`12`), but don't resample:

```
$ pitch-shifter.py -s ./samples/sample1.wav -o out.wav -p 12 --no-resample
```

To half the speed shift down an octave (`-12`), but don't resample:

```
$ pitch-shifter.py -s ./samples/sample1.wav -o out.wav -p -12 --no-resample
```

## Basic Algorithm Flow

```
Input --> Phase Vocoder (Stretch or compress by 2^(n/12)) --> resample by 2^(n/12)
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
