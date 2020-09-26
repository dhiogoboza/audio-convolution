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
-o | string | output.wav | Output audio file name
-i  | string | samples/Please_Open_The_Door_Loud.wav | Input audio file name
-ip | string | impulses/ChurchSchellingwoude/impulse.wav | Impulse audio file name
-m | enum | convolution | Function to use in convolution (fft or convolution)
-p | bool | True | Play audio after convolution finish
-d | bool | False | Enable debug logs
-c | enum | mono | Channels to use (mono or stereo)
-h |  |  | Show help
