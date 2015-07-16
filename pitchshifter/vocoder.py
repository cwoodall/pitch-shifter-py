#!python
import utilities
import numpy as np

def findPeaks(frame):
    """
    
    """
    peak_indexes = []
    K = len(frame)
    for (i, fft_bin) in enumerate(frame):
        search_indices = [i-2,i+2]
        if i < 2:
            search_indices[0] = i-i
        elif i < (K-2):
            search_indices[1] = i+(K-i)
            
        if all(fft_bin >= comp_bin for comp_bin in frame[search_indices[0]:search_indices[1]]):
            peak_indexes.append(i)
            
    return peak_indexes

def getRegionOfInfluence(peaks):
    """
    Args:
      List of peaks

    Returns:
      Array of tuples with (roi_start, roi_end) inclusive
    """
    roi = []    
    last_mid_point = 0
    for i in range(len(peaks)-1):
        current_mid_point = int((peaks[i+1] - peaks[i])/2.0) + peaks[i]
        roi.append((last_mid_point, current_mid_point))
        last_mid_point = int(current_mid_point)+1
    
    # Handle last midpoint
    roi.append((last_mid_point,None))
    return roi
        
        
class InPlacePhaseVocoder(object):
    """
    Implements a variant of the phase vocoder algorithm described in the paper:
      "NEW PHASE-VOCODER TECHNIQUES FOR PITCH-SHIFTING, HARMONIZING AND OTHER 
       EXOTIC EFFECTS" by Jean laroche and Mark Dolson
    """

    def __init__(self):
        return

    

class PhaseVocoder(object):
    """
    Implements the phase vocoder algorithm.
    
    Useage:
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
