# Adaptive AI Learning Platform
Scalable Intelligent Tutoring & Cognitive Profiling System

## Overview
Adaptive AI Learning Platform is a scalable intelligent tutoring system that dynamically adjusts question difficulty based on user performance and response-time analytics. Unlike static quiz systems, this platform models learning behavior, tracks concept-level mastery, and personalizes difficulty in real time. The architecture is modular and designed to simulate production-level EdTech systems with persistent storage.

## Core Objectives
- Personalize learning experience
- Dynamically adjust difficulty
- Track concept-level mastery
- Store persistent user performance
- Generate real-time analytics
- Provide scalable backend architecture

## Key Features
- Dynamic difficulty adjustment engine
- Concept-level mastery tracking
- Multi-user support
- Persistent storage using SQLite
- Performance analytics visualization
- Modular backend design
- Expandable question bank structure

## System Architecture
Frontend:
- Streamlit interactive interface
- Real-time analytics dashboard

Backend:
- Adaptive difficulty engine
- Mastery computation engine
- SQLite database management
- Modular service separation

Data Layer:
- Question bank with difficulty and concept tagging
- User performance tracking
- Persistent database storage

## How It Works
1. User enters a username.
2. System retrieves historical performance from database.
3. Recent performance is analyzed.
4. Difficulty is adjusted dynamically:
   - High accuracy increases difficulty
   - Low accuracy decreases difficulty
   - Moderate accuracy maintains difficulty
5. User answers question.
6. System updates mastery and performance analytics.
7. Data is stored persistently in SQLite.

## Project Structure
Adaptive-AI-Learning-Platform  
│── app.py  
│── backend/  
│   ├── database.py  
│   ├── adaptive_engine.py  
│   ├── mastery_engine.py  
│── models/  
│   ├── question_loader.py  
│── database.db  
│── requirements.txt  

## Installation
Create virtual environment:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

## Run Application
streamlit run app.py

Application runs at:
http://localhost:8501

## Database
The system automatically creates database.db to store:
- Usernames
- Performance history
- Concept mastery data
- Response-time analytics

No manual database configuration is required.

## Scalability Design
The architecture supports migration to:
- PostgreSQL or MySQL
- FastAPI backend
- REST API integration
- Cloud deployment
- Reinforcement learning-based difficulty tuning
- Advanced mastery prediction models

Backend logic is modular, allowing easy scaling and system expansion.

## Real-World Applications
- Adaptive education platforms
- Competitive exam preparation systems
- Corporate training systems
- Intelligent tutoring platforms
- AI-based personalized education engines

## Technical Stack
- Python
- Streamlit
- SQLite
- NumPy
- Pandas
- Matplotlib

## Innovation Highlights
This project demonstrates:
- Behavioral modeling
- Adaptive intelligence systems
- Concept-aware mastery tracking
- Persistent scalable backend design
- Real-time performance analytics
- Production-style modular architecture

## Author
Mohamed Mustak M  
Machine Learning & AI Enthusiast  
GitHub: https://github.com/MOHAMEDMUSTAK
