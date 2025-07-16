#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from faster_whisper import WhisperModel

model = WhisperModel("medium", compute_type="int8")  # use "small" for speed

def transcribe_audio(audio_path):
    segments, _ = model.transcribe(audio_path, language="zh")
    full_text = ''.join([seg.text for seg in segments])
    return full_text  # Already Mandarin, no conversion needed