# 🗣️ Voice Chatbot (CPU-based)

A lightweight voice chatbot that runs entirely on CPU, following a **STT → LLM → TTS** pipeline. Ideal for devices with no GPU support.

---

## 🧠 Pipeline Overview

1. **STT (Speech-to-Text)** – Converts your voice input into text.
2. **LLM (Large Language Model)** – Processes the text and generates a response.
3. **TTS (Text-to-Speech)** – Converts the LLM response back into natural-sounding speech.

---

## 📦 Required Files

To get started, make sure you have the following files:

| Component | Description | Required File |
|----------|-------------|----------------|
| LLM      | Your preferred language model | ✅ (select and integrate your own) |
| TTS Core | Core voice synthesis model    | `kokoro-v0_19.onnx` |
| TTS Data | Voice data pack               | `voices-v1.0.bin` |

> ⚠️ These files must be placed in the root directory (or your configured model path).

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Voice-Chatbot-CPU-based.git
cd Voice-Chatbot-CPU-based
````
````bash
pip install -r requirement.txt
python chatbotllamaCPP.py
````