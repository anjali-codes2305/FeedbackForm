# EduVoice – Student Feedback Portal

EduVoice is a full-stack web application designed to collect student feedback and provide administrators with a centralized view of all submissions.  
The project demonstrates clean frontend–backend integration using modern Python backend practices and a responsive user interface.

---

## Overview

The application allows students to submit feedback through a simple and intuitive form.  
All submissions are processed by a FastAPI backend, validated using Pydantic models, and stored in a structured JSON format.  
An admin panel fetches and displays all feedback dynamically using REST APIs.

---

## Key Features

### Student Module
- Submit feedback with name and message
- Clean and responsive user interface
- Instant confirmation after submission

### Admin Module
- Dedicated admin panel
- View all submitted feedback in a structured table
- Real-time data fetched from backend APIs

### Backend
- RESTful API architecture
- Data validation using Pydantic
- File-based persistence using JSON
- CORS enabled for frontend–backend communication

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Backend
- Python
- FastAPI
- Uvicorn

### Tools
- Git & GitHub
- VS Code

---
Student Interface
      ↓
JavaScript Fetch API
      ↓
FastAPI Backend
      ↓
JSON Data Storage
      ↓
Admin Panel View
