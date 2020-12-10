# Speech emotion recognition



## Data
I used audio files (16bit, 48kHz .wav) from the [RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)](https://zenodo.org/record/1188976#.X152FYaxWis). There are 1440 recordings of 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. Speech includes calm, happy, sad, angry, fearful, surprise, and disgust expressions. Each expression is produced at two levels of emotional intensity (normal, strong), with an additional neutral expression.

Filename identifiers 
- Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
- Vocal channel (01 = speech, 02 = song).
- Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
- Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
- Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
- Repetition (01 = 1st repetition, 02 = 2nd repetition).
- Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

## Features
y: Emotion
X: 
- MFCC (Mel-Frequency Cepstral Coefficients)
- Zero-crossing rate: a measure of number of times in a given time interval/frame that the amplitude of the speech signals passes through a value of zero. 


## Models
- Convolutional Neural Networks
- Recurrent Neural Networks
- Hidden Markov Models

## How to use