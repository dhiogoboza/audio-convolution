# Audio convolution tests

Convolve input wav audio with an wav impulse audio. Impulses extracted from [https://fokkie.home.xs4all.nl/IR.htm](https://fokkie.home.xs4all.nl/IR.htm).

## Requirements
 - [pipenv](https://pypi.org/project/pipenv/)

## Usage
```
pipenv shell
python main.py
```

## Options

Option | Type | Default | Description
------ | ---- | ------- | -------
output | string | output.wav | Output audio file name
input  | string | samples/001.wav | Input audio file name
impulse | string | impulses/ChurchSchellingwoude/impulse.wav | Impulse audio file name
method | enum(fft, convolution) | convolution | Function to use in convolution
play | boolean | True | Play audio after convolution finish
debug | boolean | False | Enable debug logs

