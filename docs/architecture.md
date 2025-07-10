# YCG Module Map

## 🎯 Goal:
Fully automated YouTube content generator using GPT (text), TTS (voice), and FFmpeg (video)

---

## 🔧 Core Modules

1. **Script Generator (GPT-based)**
   - Input: Topic or prompt
   - Output: YouTube-ready script
   - Tools: OpenAI API

2. **Voiceover Generator (TTS)**
   - Input: Script
   - Output: MP3 or WAV narration
   - Tools: ElevenLabs, pyttsx3, or gTTS

3. **Video Synthesizer**
   - Input: Audio + visuals
   - Output: Final .mp4 video
   - Tools: FFmpeg, image bank, captions, transitions

---

## 🧰 Supporting Modules

- `utils/` — shared helpers (e.g. file I/O, config loading)
- `config/` — settings and keys
- `assets/` — raw media files
- `tests/` — future testing support

---

## 📌 Planned Workflow

1. `main.py` triggers end-to-end pipeline
2. Each module can be tested individually
3. Intermediate outputs are cached
