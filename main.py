import argparse
import numpy
import wavfile

from loguru import logger
from playsound import playsound
from scipy import signal

def convolve(args):
	sample_res = wavfile.read(args['input'], normalized=True, forcestereo=True)
	impulse_res = wavfile.read(args['impulse'], normalized=True, forcestereo=True)

	debug = args['debug']

	if debug:
		logger.debug('sample data: \n{data}', data=sample_res[1])
		logger.debug('impulse_res: \n{data}', data=impulse_res[1])

	sr = sample_res[1]#utility.pcm2float(sample_res[1], 'float64')
	ir = impulse_res[1]#utility.pcm2float(impulse_res[1], 'float64')
	
	if debug:
		logger.debug('sample data as float: \n{data}', data=sr)

	if args['output'] == 'convolve':
		# use numpy convolve
		logger.info('Using numpy.convolve')
		out_0 = numpy.convolve(sr[:, 0], ir[:, 0])
		out_1 = numpy.convolve(sr[:, 1], ir[:, 1])
	else:
		# use scipy fftconvolve
		logger.info('Using scipy.signal.fftconvolve')
		out_0 = signal.fftconvolve(sr[:, 0], ir[:, 0])
		out_1 = signal.fftconvolve(sr[:, 1], ir[:, 1])

	# merge channels
	out = numpy.vstack((out_0, out_1)).T

	# save output
	wavfile.write(args['output'], sample_res[0], out, normalized=True)
	
	if args['play']:
		playsound(args['output'])

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', '-i', default='samples/Please_Open_The_Door_Loud.wav')
	parser.add_argument('--output', '-o', default='output.wav')
	parser.add_argument('--impulse', '-ip', default='impulses/ChurchSchellingwoude/impulse.wav')
	parser.add_argument('--method', '-m', choices=['fft', 'convolution'], default="fft")
	parser.add_argument('--play', '-p', default=False)
	parser.add_argument('--debug', '-d', default=False)
	
	args = vars(parser.parse_args())
	if not args['impulse'].endswith('.wav'):
		args['impulse'] = args['impulse'] + '/impulse.wav'

	convolve(args)

if __name__ == "__main__":
	main()
