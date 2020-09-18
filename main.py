#from scipy.io import wavfile
from scipy import signal

import numpy
import wavfile

#from scipy.io import wavfile
import utility
#fs, sig = wavfile.read('samples/001.wav')
#normalized = utility.pcm2float(sig, 'float32')
#print("normalized", normalized)


sample_res = wavfile.read('samples/001.wav')
impulse_res = wavfile.read('impulses/Church_Schellingwoude/Church_Schellingwoude.wav')

print("Sample rate", sample_res[0])
print("Impulse rate", impulse_res[0])

#output_data = numpy.convolve(numpy.ndarray.flatten(impulse_res[1]), numpy.ndarray.flatten(sample_res[1]))

sr = utility.pcm2float(sample_res[1], 'float32')
ir = utility.pcm2float(impulse_res[1], 'float32')

out_0 = signal.fftconvolve(sr[:, 1], ir[:, 1])
out_1 = signal.fftconvolve(sr[:, 1], ir[:, 1])
out = numpy.vstack((utility.float2pcm(out_0, 'int16'), utility.float2pcm(out_1, 'int16'))).T

# save output
wavfile.write("output.wav", sample_res[0], out)

"""
output_data = numpy.zeros((len(sample_res[1]), 2))
impulse_index = 0
current_sample = 0
for sample_el in sample_res[1]:
	#print("impulse_res[1][impulse_index]", impulse_res[1][impulse_index])
	#print("sample_el", sample_el)

	output_data[current_sample][0] = impulse_res[1][impulse_index][0] * sample_el[0]
	output_data[current_sample][1] = impulse_res[1][impulse_index][1] * sample_el[1]

	impulse_index += 1
	current_sample += 1
	if impulse_index == len(impulse_res[1]):
		impulse_index = 0

# save output
print("sample_res", sample_res[1])
print("impulse_res", impulse_res[1])
print("out", output_data)
wavfile.write("output.wav", sample_res[0], output_data)
"""
