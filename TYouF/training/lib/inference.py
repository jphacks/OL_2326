# -*- coding: utf-8 -*-
"""Inference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NjlRES3Qvx9fkXMEvBx6u2RqDB8BbhlB
"""

import sys
sys.path.append('/path/to/ffmpeg')

# coding= UTF-8
import numpy as np
import sklearn
from sklearn.svm import SVC, LinearSVC
import pickle
from pydub import AudioSegment
import os

# coding= UTF-8
import glob
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import soundfile as sf
import tempfile


EXAMPLE_FILE = "/Users/cmiyoshi/Documents/JPHACKS2023/OL_2326/TYouF/training/lib/SnapSave.io - How to THINK in English _ No More Translating in Your Head! (320 kbps).mp3"  # 音声ファイルのパスを指定

##Return audio features
def feature_extraction(file_name):
    #X, sample_rate = sf.read(file_name, dtype='float32')
    X , sample_rate = librosa.load(file_name, sr=None) #Can also load file using librosa
    if X.ndim > 1:
        X = X[:,0]
    X = X.T

    ## stFourier Transform
    stft = np.abs(librosa.stft(X))

    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=20).T, axis=0) #Returns N_mel coefs
    rmse = np.mean(librosa.feature.rms(y=X).T, axis=0) #RMS Energy for each Frame (Stanford's). Returns 1 value
    spectral_flux = np.mean(librosa.onset.onset_strength(y=X, sr=sample_rate).T, axis=0) #Spectral Flux (Stanford's). Returns 1 Value
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=X).T, axis=0) #Returns 1 value

    #mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0) #Returns 128 values
    #chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0) #Returns 12 values
    #contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0) #Returns 7 values
    #tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T, axis=0) #tonal centroid features Returns 6 values

    ##Return computed audio features
    return mfccs, rmse, spectral_flux, zcr

# Audio parsing: Function makes call for feature extraction and returns array with features and labels
def parse_audio_files(file_name): # Audio Format

    n_mfccs = 20 # This variable is tunneable with each run
    number_of_features = 3 + n_mfccs
    #number_of_features = 154 + n_mfccs # 154 are the total values returned by rest of computed features
    features, labels = np.empty((0,number_of_features)), np.empty(0)
    ##Extract features for each audio file
    mfccs, rmse, spectral_flux, zcr = feature_extraction(file_name)
    extracted_features = np.hstack([mfccs, rmse, spectral_flux, zcr])
    #print "Total Extracted Features: ", len(extracted_features) #This helps us identify really how many features are being computed
    features = np.vstack([features, extracted_features]) #Stack arrays in sequence vertically (row wise).
    label = 100
    labels = np.append(labels, label)
    #print("Extracted features from %s, done" % (file_name))
    return np.array(features), np.array(labels, dtype = np.int64) ## arrays with features and corresponding labels for each audio

def split_audio(file_path, segment_duration=5000):
    audio = AudioSegment.from_file(file_path)
    segment_count = len(audio) // segment_duration
    #print(segment_count)
    result_list = []
    for i in range(segment_count):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        segment = audio[start_time:end_time]
        # セグメントごとに処理を行う
        # pydubを使用して一時的なmp3ファイルに変換
        temp_wav_file = "./temp.mp3"
        segment.export(temp_wav_file, format="mp3")
        features, labels = parse_audio_files(temp_wav_file)
        result_list.append(features)
        ##delete
    os.remove(temp_wav_file)
    return result_list

def Inference_result(file_path):
  result = split_audio(file_path)
  # coding= UTF-8
  # Fix random seed number
  np.random.seed(7)

  with open('/Users/cmiyoshi/Documents/JPHACKS2023/OL_2326/TYouF/training/lib/model.pickle', mode='rb') as f:
      clf = pickle.load(f)

  answers = []
  for result_i in result:
    answer = clf.predict(result_i)
    answers.append(int(answer))
  return sum(answers)

print(Inference_result(EXAMPLE_FILE))
