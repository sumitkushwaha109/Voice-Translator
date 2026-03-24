# 🎙 Voice Translator (Full Stack Project)

A real-time Voice Translator web application that converts speech → text → translated text → audio output.

Built using:

*  OpenAI Whisper (Speech-to-Text)
*  Argos Translate (Offline Translation)
*  gTTS (Text-to-Speech)
*  Django REST Framework (Backend)
*  HTML + JS (Frontend)

---

#  Features

*  Record voice from browser
*  Convert speech to text (Whisper)
*  Translate between languages (Argos)
*  Generate audio output (gTTS)
*  Language swap support
*  Audio playback in UI
*  Modern Dark UI

---

#  Setup Instructions

## 2. Install Python (Important)

👉 This project works best with **Python 3.11** (recommended)

### Mac (using brew):

```
brew install python@3.11
```

### Check version:

```
python3.11 --version
```

---

## 3. Create Virtual Environment

 Make sure you use Python 3.11

```
python3.11 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate      # Windows
```

---

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate      # Windows
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```
## 4. Install FFmpeg (Required)

Mac:

```
brew install ffmpeg
```

Ubuntu:

```
sudo apt install ffmpeg
```

Windows:
Download from: [https://ffmpeg.org](https://ffmpeg.org)

---

## 5. Run Backend

```
python manage.py runserver
```

---

## 6. Run Frontend

```
python3 -m http.server 5500
```

Then open:

```
http://localhost:5500
```


#  .gitignore

```
venv/
__pycache__/
*.pyc
.env
media/

