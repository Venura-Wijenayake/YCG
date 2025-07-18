# 🎬 YCG — YouTube Content Generator

An AI-powered pipeline that takes your idea from **topic** to **talking thumbnail**.  
YCG turns raw prompts into fully voiced, fully edited YouTube videos — all with zero editing skills required.

---

## ⚡ What It Does

- 🔍 **Smart Topic Selection** — choose your own or generate it on the fly  
- 🧠 **Scriptwriting** — powered by GPT and enhanced with custom tone injection  
- 🎙️ **Voiceover Generation** — realistic narration using Google TTS or ElevenLabs  
- 🖼️ **Visual Assembly** — pair narration with imagery (via APIs or static fallback)  
- 🎞️ **Video Compilation** — output clean, synced MP4s using `ffmpeg`  
- 🖼️ **Optional Add-ons** — auto-thumbnailing, SEO titles, and upload automation

---

## 🛠️ Tech Stack

- 🐍 Python
- 🤖 OpenAI GPT (for scriptwriting)
- 🗣️ pyttsx3, Google TTS, ElevenLabs (for voice generation)
- 🎬 ffmpeg (video rendering)
- ⚙️ YAML + modular Python design (clean config + scale support)

---

## 🚧 Project Status

- ✅ MVP architecture scaffolded  
- ✅ GitHub repo initialized  
- ✅ Script generation with style control  
- ✅ Demo runs and prompt-to-script tested  
- 🔜 Voice layer and final video assembly

---

## 💡 Vision

YCG isn’t just a gimmick — it’s a full-stack, modular content automation engine.  
Built to support batch pipelines, stylized series, and even auto-upload workflows.

> One topic. One command. One fully edited video.

---

## 📎 Quick Start

```bash
git clone https://github.com/your-username/ycg.git
cd ycg
pip install -r requirements.txt
python main.py

```

🖼️ Demo Screenshots
Step 1: User Prompt Flow
<img src="https://i.imgur.com/cU22zrK.png" alt="Prompt Input Screenshot" width="700"/>
Step 2: Script Generation Triggered
<img src="https://i.imgur.com/JwZlTEH.png" alt="Script Generation Screenshot" width="700"/>



