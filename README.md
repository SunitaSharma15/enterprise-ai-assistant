# Enterprise AI Assistant 

An AI-powered enterprise knowledge assistant built with **Angular + FastAPI + Chroma + RAG**.

Users can upload company documents, ask questions in natural language, and receive accurate answers grounded in document context.

---

## Features

* Upload documents (PDF / TXT / DOCX)
* Ask questions from uploaded files
* Semantic search using embeddings
* RAG (Retrieval-Augmented Generation)
* FastAPI REST APIs
* Angular frontend
* Docker support
* Free-tier deployment ready

---

## Tech Stack

### Frontend

* Angular

### Backend

* FastAPI
* Python

### AI Layer

* LLM APIs / Open models
* Embeddings

### Database

* Chroma Vector DB

### DevOps

* GitHub
* Docker
* Render / Railway

---

## Project Structure

```text
enterprise-ai-assistant/
│── frontend-angular/
│── ai-service/
│── README.md
```

---

## Getting Started

### Clone Repo

```bash
git clone <your-repo-url>
cd enterprise-ai-assistant
```

### Frontend Setup

```bash
cd frontend-angular
npm install
ng serve
```

Frontend runs on:
`http://localhost:4200`

### Backend Setup

```bash
cd ai-service
python -m venv venv
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:
`http://localhost:8000`

---

## API Endpoints

### Health Check

`GET /health`

### Ask AI

`POST /ask`

---

## Use Cases

* HR Policy Assistant
* Internal Knowledge Search
* Product Documentation Bot
* Support Assistant
* Employee Onboarding Bot

---

## Skills Demonstrated

* Prompt Engineering
* LLM Integration
* Embeddings
* Vector Search
* RAG
* REST APIs
* Full Stack Development
* Deployment

---

## Roadmap

* [x] Project Setup
* [ ] Angular ↔ FastAPI Integration
* [ ] First AI Endpoint
* [ ] Embeddings + Chroma
* [ ] RAG Chat
* [ ] Authentication
* [ ] Docker Deployment

---

## Author

Built by Sunita Sharma (Java Full Stack Developer) transitioning into AI Engineering.
