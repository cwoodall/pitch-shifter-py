#!python
import utilities
import numpy as np

class PhaseVocoder(object):
    def __init__(self, ihop, ohop):
        self.input_hop = ihop
        self.output_hop = ohop
        self.last_phase = 0
        self.phase_accumulator = 0

        
    def reset(self):
        self.last_phase = 0
        self.phase_accumulator = 0

    def sendFrame(self, frame):
        omega_bins = 2*np.pi*np.arange(len(frame))/len(frame)
        magnitude, phase = utilities.complex_cartesianToPolar(frame)

        delta_phase = phase - self.last_phase
        self.last_phase = phase

        delta_phase_unwrapped =  delta_phase - self.input_hop * omega_bins
        delta_phase_rewrapped = np.mod(delta_phase_unwrapped + np.pi, 2*np.pi) - np.pi
        
        true_freq = omega_bins + delta_phase_rewrapped/self.input_hop
        
        self.phase_accumulator += self.output_hop * true_freq
        
        return utilities.complex_polarToCartesian(magnitude, self.phase_accumulator)

    def sendFrames(self, frames):
        for frame in frames:
            yield self.sendFrame(frame)
