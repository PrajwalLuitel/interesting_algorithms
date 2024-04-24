"""
The FFT is a method to compute the Discrete Fourier Transform (DFT) and its inverse. Fourier analysis converts a signal 
from its original domain (often time or space) to a representation in the frequency domain and vice versa. The DFT is 
obtained by decomposing a sequence of values into components of different frequencies.

This algorithm has a wide range of applications in computer science and engineering such as:

Digital Signal Processing
Image Analysis
Solving Partial Differential Equations
Polynomial Multiplication and Division
Data Compression
And many more
The FFT algorithm has dramatically improved the efficiency of computations involving Fourier transforms, contributing 
significantly to advances in a wide range of applications. It’s a beautiful example of how an efficient algorithm can 
lead to practical advancements in diverse fields.
"""

import numpy as np


def fft(x):
    N = x.shape[0]
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [
        even[k] - T[k] for k in range(N // 2)
    ]


# Test
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
X = fft(x)
print("FFT:", X)


"""
This code first checks if the input is of size 1. If so, it returns the input itself as the Fourier Transform. 
Otherwise, it recursively applies the FFT to the even and odd indexed elements of the input. 
Then it combines these results to produce the Fourier Transform of the original input.
"""


# Additionally, libraries can be utilized for the same purpose. One of the examples is:

import numpy as np

# Test
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
X = np.fft.fft(x)
print("FFT:", X)
