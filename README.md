# 🎬 YCG — YouTube Content Generator

An AI-powered pipeline that takes your idea from **topic** to **talking thumbnail**.  
YCG turns raw prompts into fully voiced, fully edited YouTube videos — all with zero editing skills required.

---

## ⚡ What It Does

- 🔍 **Smart Topic Selection** — choose your own or generate it on the fly  
- 🧠 **Scriptwriting** — powered by GPT and enhanced with custom tone injection  
- 🎙️ **Voiceover Generation** — realistic narration using Google TTS or ElevenLabs  
- 🖼️ **Visual Assembly** — pair narration with imagery (APIs or static)  
- 🎞️ **Video Compilation** — output clean, synced MP4s using ffmpeg  
- 🖼️ **Optional Add-ons** — auto-thumbnailing, SEO titles, even upload automation

---

## 🛠️ Tech Stack

- 🐍 Python
- 🤖 OpenAI GPT (for scriptwriting)
- 🗣️ pyttsx3, Google TTS, ElevenLabs (for voice)
- 🎬 ffmpeg (video rendering)
- ⚙️ YAML + modular Python (easy to configure and scale)

---

## 🚧 Project Status

- ✅ MVP architecture scaffolded  
- ✅ GitHub repo initialized  
- 🔜 **Next:** Script generation module + voice layer integration

---

## 💡 Vision

YCG isn’t just a gimmick — it’s a full-stack, modular content automation engine.  
Built to support batch pipelines, stylized series, and even auto-upload workflows.

> One topic. One command. One fully edited video.

---

## 📎 Quick Start (coming soon)

```bash
git clone https://github.com/your-username/ycg.git
cd ycg
pip install -r requirements.txt
python main.py


### Step 1: User Prompt Flow
![Prompt Input](assets/images/A1.jpg)

### Step 2: Generation Starts
![Generation Trigger](assets/images/A2.jpg)