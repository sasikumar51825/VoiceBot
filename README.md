VoiceBot Interview Practice
Overview

VoiceBot Interview Practice is an AI-powered voice assistant that helps users practice common interview questions and receive instant feedback to improve their answers.
It consists of two main components:

Voice Interaction Module

Uses Whisper for offline speech-to-text.

Records user answers via microphone.

Converts feedback text to speech using pyttsx3.

AI Feedback Module

Uses GPT4All for generating constructive feedback.

Evaluates answers with concise scoring and improvement suggestions.

Provides a revised example answer for guidance.

Features

Voice-based question answering.

Real-time AI feedback with evaluation, weak points, and improvement tips.

Text-to-speech output for spoken feedback.

Fully offline capabilities using local models.

Easy to customize question bank and recording settings.

Technologies

Python

Whisper (speech-to-text)

GPT4All (AI feedback)

pyttsx3 (text-to-speech)

sounddevice & NumPy (audio recording)

Customize

Add or edit questions in chatbot.py

Change recording time in stt.py

Use a different GPT model in models/
