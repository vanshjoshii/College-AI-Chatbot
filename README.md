# Colege Chatbot(MIT-WPU Assistant)

This is a lightweight Flask-based chatbot prototype built around Google Generative AI (Gemini). The interface is customised for MIT World Peace University (MIT-WPU) and includes a responsive in-page chat widget (desktop + mobile), quick replies, rich message rendering (Markdown → HTML), avatars, and a typing/loading animation.

NOTE: This repository contains a demo integration using the `google.generativeai` package. The app currently sends user queries directly to Gemini and returns the model response. If you want the assistant to be MIT-WPU–specific and ground answers in university documents, consider adding a Retrieval-Augmented Generation (RAG) pipeline and a vector store (instructions below).

## Project structure

- `app.py` — Flask server + /ask endpoint. Uses Google Generative AI to generate responses and converts Markdown to HTML.
- `templates/index.html` — Chat UI (HTML/CSS/JS). This is the primary front-end for the chat widget.
- `static/` — static assets (background, logo, avatars).
- `utils.py` — helper utilities (if present).

## Features

- Responsive chat widget (desktop & mobile) with a persistent toggle button.
- Quick replies, carousel/card-ready layout.
- Markdown conversion on the server (so bot responses support bold, lists, links, etc.).
- Loading/typing animation.

## Prerequisites

- Python 3.10+ (3.12 used while developing)
- A Google Generative AI API key (Gemini). Keep it secret. Do not commit your API key to source control.

Recommended (create a virtual environment):

Windows (cmd.exe):

```
cd C:\Users\Vansh\Documents\Chatbot-MiniProject
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

Create `requirements.txt` (example) and install. Example packages used in this project:

```
Flask
google-generativeai
markdown
```

Install with pip:

```
pip install -r requirements.txt
```

If you plan to add RAG/vector search later, you may also need `langchain`, `faiss-cpu`, `pymupdf`, etc.

## Configuration

The easiest quick-start approach is to temporarily add your API key directly in `app.py` where `genai.configure(api_key=...)` is called. Recommended production approach is to use an environment variable and update `app.py` to read it.

Example (recommended change in `app.py`):

```python
import os
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise RuntimeError('Set GEMINI_API_KEY environment variable')
genai.configure(api_key=api_key)
```

On Windows (cmd.exe) set the variable for the session:

```
set GEMINI_API_KEY=your_api_key_here
python app.py
```

Or permanently (PowerShell / system settings) depending on your preference.

## Run the app (development)

After installing dependencies and configuring the API key:

```
cd C:\Users\Vansh\Documents\Chatbot-MiniProject
python app.py
```

Open http://127.0.0.1:5000/ in your browser.
