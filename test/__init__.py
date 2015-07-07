#!python

from pitchshifter import *

class TestUtilities(object):
    def test_complex_polarToCartesian_correctResults(self):
        r = 1.4142     # magnitude
        theta = 0.7854 # radians
        results = complex_polarToCartesian(r, theta)
        
        expected_results = 1 + 1j
        assert abs(results.real - expected_results.real) < .01
        assert abs(expected_results.imag - results.imag) < .01

class TestSTFT(object):
    def test_stft_correct_results(self):
        assert False

