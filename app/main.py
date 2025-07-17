#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import streamlit as st
import tempfile
from core import speech_to_text, scoring, dialogue_manager

st.set_page_config(page_title="Cognitive Agent", layout="centered")

st.title("🧠 語音認知評估助手")

dm = dialogue_manager.DialogueManager()

if "history" not in st.session_state:
    st.session_state["history"] = []
    st.session_state["scores"] = []

st.audio_file = st.file_uploader("上傳你的語音回答", type=["mp3", "wav", "m4a"])

if st.audio_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(st.audio_file.read())
        tmp_path = tmp.name

    st.info("⏳ 辨識中...")
    transcript = speech_to_text.transcribe_audio(tmp_path)
    st.success("✅ 文字轉換完成！")
    st.write("📝 回答內容：", transcript)

    score = scoring.evaluate_response(transcript)
    st.session_state["history"].append((dm.current['text'], transcript))
    st.session_state["scores"].append(score)

    st.subheader("📊 分數結果")
    st.json(score)

    st.markdown("---")
    st.subheader("🧑‍⚕️ 下一個問題")
    st.write(dm.get_next())
