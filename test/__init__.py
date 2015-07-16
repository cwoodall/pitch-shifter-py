#!python

from pitchshifter import *
import numpy as np

class TestInPlacePhaseVocoder(object):
    def test_findPeaks_simple(self):
        res = findPeaks([1,2,3,2,1])
        
        assert len(res) == 1
        assert res[0] == 2

    def test_findPeaks_earlyPeak(self):
        res = findPeaks(
            [8,1,2,4,3,2,1,1])

        print(res)
        assert len(res) == 2
        assert res[0] == 0
        assert res[1] == 3
    
    def test_getRegionOfInfluence_3peaks(self):
        res = getRegionOfInfluence([0,8,21])
        assert res == [(0,4), (5,14), (15, None)]
        
class TestUtilities(object):
    def test_complex_polarToCartesian_correctResults(self):
        r = 1.4142     # magnitude
        theta = 0.7854 # radians
        results = complex_polarToCartesian(r, theta)
        
        expected_results = 1 + 1j
        assert abs(results.real - expected_results.real) < .01
        assert abs(expected_results.imag - results.imag) < .01

    def test_complex_cartesianToPolar_correctResults(self):
        results = complex_cartesianToPolar(1+1j)
        
        expected_results = (1.4142, .7854)
        assert abs(results[0] - expected_results[0]) < .001
        assert abs(results[1] - expected_results[1]) < .001

    def test_complex_polarToCartesian_arrayCorrectResults(self):
        rs = np.asarray([1.4142 for i in range(10)])
        thetas = np.asarray([0.7854 for i in range(10)])
        
        results = complex_polarToCartesian(rs, thetas)
        
        expected_results = 1 + 1j
        for result in results:
            assert abs(result.real - expected_results.real) < .01
            assert abs(expected_results.imag - result.imag) < .01

    def test_complex_cartesianToPolar_arrayCorrectResults(self):
        rs, thetas= complex_cartesianToPolar(np.asarray([1+1j for i in range(10)]))

        expected_results = (1.4142, .7854)
        for r in rs:
            assert abs(r - expected_results[0]) < .001

        for theta in thetas:
            assert abs(theta - expected_results[1]) < .001
    
#class TestSTFT(object):
#    def test_stft_correct_results(self):
#        assert False

