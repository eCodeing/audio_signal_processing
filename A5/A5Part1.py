import numpy as np
from scipy.signal import get_window
import math
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import dftModel as DFT
import utilFunctions as UF

""" 
A5-Part-1: Minimizing the frequency estimation error of a sinusoid

Write a function that estimates the frequency of a sinusoidal signal at a given time instant. The 
function should return the estimated frequency in Hz, together with the window size and the FFT 
size used in the analysis.  

The input arguments to the function are the wav file name including the path (inputFile) containing 
the sinusoidal signal, and the frequency of the sinusoid in Hz (f). The frequency of the input sinusoid  
can range between 100Hz and 2000Hz. The function should return a three element tuple of the estimated 
frequency of the sinusoid (fEst), the window size (M) and the FFT size (N) used.

The input wav file is a stationary audio signal consisting of a single sinusoid of length 1 second. 
Since the signal is stationary you can just perform the analysis in a single frame, for example in 
the middle of the sound file (time equal to .5 seconds). The analysis process would be to first select 
a fragment of the signal equal to the window size, M, centered at .5 seconds, then compute the DFT 
using the dftAnal function, and finally use the peakDetection and peakInterp functions to obtain the 
frequency value of the sinusoid.

Use a Blackman window for analysis and a magnitude threshold t = -40 dB for peak picking. The window
size and FFT size should be chosen such that the difference between the true frequency (f) and the 
estimated frequency (fEst) is less than 0.05 Hz for the entire allowed frequency range of the input 
sinusoid. The window size should be the minimum positive integer of the form 100*k + 1 (where k is a 
positive integer) for which the frequency estimation error is < 0.05 Hz. For a window size M, take the
FFT size (N) to be the smallest power of 2 larger than M. 

HINT: If the specified frequency range would have been 440-8000 Hz, the parameter values that satisfy 
the required conditions would be M = 1101, N = 2048. Note that for a different frequency range, like 
the one specified in the question, this value of M and N might not work. 

"""
def minFreqEstErr(inputFile, f):
    """
    Inputs:
            inputFile (string) = wav file including the path
            f (float) = frequency of the sinusoid present in the input audio signal (Hz)
    Output:
            fEst (float) = Estimated frequency of the sinusoid (Hz)
            M (int) = Window size
            N (int) = FFT size
    """
    # analysis parameters:
    window = 'blackman'
    t = -40
    
    ### Your code here
    (fs, x) = UF.wavread(inputFile)    

    numbins = 6
    k = 21
    #M = int(numbins * fs / f)
    
    
    M = (100*k) + 1

    N = int(pow(2, np.ceil(np.log2(M))))  

    w = get_window(window, M)

    hx = len(x) / 2
    x1 = x[(.5*fs)-(M/2):(.5*fs)+((M/2)+1)]
    #x1 = x[hx-(M/2):hx+(M/2)+1]
        
    mX, pX = DFT.dftAnal(x1, w, N)
    ploc = UF.peakDetection(mX, t)
    pmag = mX[ploc]

    (iploc, ipmag, ipphase) = UF.peakInterp(mX, pX, ploc)

    fEst = (fs * float(np.sum(iploc))) / float(N)
    
    esterror = np.abs(fEst - f)
    print esterror

    return (fEst, M, N)


def generateSine(f0):
    A = .8
    phi = np.pi/2
    fs = 44100
    t = np.arange(0.0, 1.0, 1.0/fs)
    x = A * np.cos(2*np.pi*f0*t+phi)

    return x

def test():
    window = 'blackman'
    t = -40
    fs = 44100
    a = [101, 200, 440]
    k = 1
    matched = False
    while True:
        M = (100*k) + 1

        N = int(pow(2, np.ceil(np.log2(M))))  

        w = get_window(window, M)

        for f in np.arange(100,8000):
        #for i in range(len(a)):
            #f = a[i]
            x = generateSine(f)

            hx = len(x) / 2
            x1 = x[(.5*fs)-(M/2):(.5*fs)+((M/2)+1)]
            #x1 = x[hx-(M/2):hx+(M/2)+1]
        
            mX, pX = DFT.dftAnal(x1, w, N)
            ploc = UF.peakDetection(mX, t)
            pmag = mX[ploc]

            (iploc, ipmag, ipphase) = UF.peakInterp(mX, pX, ploc)

            fEst = (fs * float(np.sum(iploc))) / float(N)
            esterror = np.abs(fEst - f)
            print esterror

            if (esterror > 0.05):
                matched = False
                break
            else:
                matched = True
        
        if matched:
            break
        else:
            k += 1
    
    print fEst 
    print k
    print M
    print N

#test()  
#(fEst, M, N) = minFreqEstErr("../../sounds/sine-440.wav", 440.0)
#(fEst, M, N) = minFreqEstErr("../../sounds/sine-101.wav", 101.0)
#(fEst, M, N) = minFreqEstErr("../../sounds/sine-200.wav", 200.0) 
        
    
       

         

