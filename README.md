# Audio convolution tests

Convolve input wav audio with an wav impulse audio. Impulses extracted from [https://fokkie.home.xs4all.nl/IR.htm](https://fokkie.home.xs4all.nl/IR.htm). Some examples available at: [https://dhiogoboza.github.io/audio-convolution/](https://dhiogoboza.github.io/audio-convolution/).

## Requirements
 - [pipenv](https://pypi.org/project/pipenv/)

## Usage
```
pipenv shell
python main.py [options]
```

## Options

Option | Type | Default | Description
------ | ---- | ------- | -------
-output | string | output.wav | Output audio file name
-input  | string | samples/Please_Open_The_Door_Loud.wav | Input audio file name
-impulse | string | impulses/ChurchSchellingwoude/impulse.wav | Impulse audio file name
-method | enum | convolution | Function to use in convolution (fft or convolution)
-play | boolean | True | Play audio after convolution finish
-debug | boolean | False | Enable debug logs

