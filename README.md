# My Chat Website

A simple chat website built with Python and Flask.

## Features

- Home page
- Login page
- Flask backend
- Ready for Render deployment
- Simple green terminal theme

## Requirements

- Python 3.10+
- Flask
- Gunicorn

## Installation

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Deploy on Render

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

## Project Structure

```
.
├── app.py
├── requirements.txt
├── render.yaml
└── README.md
```

## License

This project is for educational purposes.
