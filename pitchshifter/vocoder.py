#!python
import utilities
import numpy as np

class PhaseVocoder(object):
    """
    Implements the phase vocoder algorithm.
    
    Usage:
        from phaseshifter import PhaseVocoder, stft
        vocoder = PhaseVocoder(HOP, HOP_OUT)
        phase_corrected_frames = [frame for frame in vocoder.sendFrames(frames)]
        
    Attributes:
        input_hop: Input hop distance/size
        output_hop: Output hop distance/size
        last_phase: numpy array of all of the previous frames phase information.
        phase_accumulator: numpy array of accumulated phases.
    """
    
    def __init__(self, ihop, ohop):
        """
        Initialize the phase vocoder with the input and output hop sizes desired.
        
        Args:
            ihop: input hop size
            ohop: output hop size
        """
        self.input_hop = int(ihop)
        self.output_hop = int(ohop)
        self.reset()
        
    def reset(self):
        """
        Reset the phase accumulator and the previous phase stored to 0.
        """
        self.last_phase = 0
        self.phase_accumulator = 0

    def sendFrame(self, frame):
        """
        Send a single frame to the phase vocoder
        
        Args:
            frame: frame of FFT information.
            
        Returns: phase corrected frame
        """
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
        """
        A generator function for processing a group of frames.
        
        Args:
            frames: an array of numpy arrays containing frequency domain information.
            
        Returns: Each iteration yields the phase correction for the current frame.
        """
        for frame in frames:
            yield self.sendFrame(frame)
