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
    stereo = args['channels'] == 'stereo'

    if debug:
        logger.debug('sample data: \n{data}', data=sample_res[1])
        logger.debug('impulse_res: \n{data}', data=impulse_res[1])

    sr = sample_res[1]
    ir = impulse_res[1]

    if debug:
        logger.debug('sample data as float: \n{data}', data=sr)

    if args['output'] == 'convolve':
        # use numpy convolve
        logger.info('Using numpy.convolve')
        out_0 = numpy.convolve(sr[:, 0], ir[:, 0])
        if stereo:
            out_1 = numpy.convolve(sr[:, 1], ir[:, 1])
    else:
        # use scipy fftconvolve
        logger.info('Using scipy.signal.fftconvolve')
        out_0 = signal.fftconvolve(sr[:, 0], ir[:, 0])
        if stereo:
            out_1 = signal.fftconvolve(sr[:, 1], ir[:, 1])

    if stereo:
        # merge channels
        out = numpy.vstack((out_0, out_1)).T
    else:
        out = out_0.T

    # save output
    wavfile.write(args['output'], sample_res[0], out, normalized=True)

    if args['play']:
        playsound(args['output'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='samples/Please_Open_The_Door_Loud.wav', help='Input audio file name')
    parser.add_argument('--output', '-o', default='output.wav', help='Output audio file name')
    parser.add_argument('--impulse', '-ip', default='impulses/ChurchSchellingwoude/impulse.wav', help='Impulse audio file name')
    parser.add_argument('--method', '-m', choices=['fft', 'convolution'], default='fft', help='Function to use in convolution')
    parser.add_argument('--play', '-p', default=True, help='Play audio after convolution finish')
    parser.add_argument('--debug', '-d', default=False, help='Enable debug logs')
    parser.add_argument('--channels', '-c', choices=['mono', 'stereo'], default='mono', help='Channels to use')

    args = vars(parser.parse_args())
    if not args['impulse'].endswith('.wav'):
        args['impulse'] = args['impulse'] + '/impulse.wav'

    convolve(args)

if __name__ == '__main__':
    main()
