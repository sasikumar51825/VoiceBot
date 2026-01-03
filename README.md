# VoiceBot Interview Practice

## Overview
VoiceBot Interview Practice allows users to speak their answers to interview questions and get real-time AI guidance.

It consists of two main components:

**Voice Interaction Module**  
- Uses Whisper for offline speech-to-text.  
- Records user answers via microphone.  
- Converts feedback text to speech using pyttsx3.  

**AI Feedback Module**  
- Uses GPT4All for generating constructive feedback.  
- Evaluates answers with concise scoring and improvement suggestions.  
- Provides a revised example answer for guidance.  

---

## Features
- Voice-based question answering.  
- Real-time AI feedback with evaluation, weak points, and improvement tips.  
- Text-to-speech output for spoken feedback.  
- Fully offline capabilities using local models.  
- Easy to customize question bank and recording settings.  

---

## Technologies
- **Python** – Core programming language.  
- **Whisper** – Offline speech-to-text.  
- **GPT4All** – Local LLM for feedback generation.  
- **pyttsx3** – Text-to-speech engine.  
- **sounddevice & NumPy** – Audio recording and processing.  

