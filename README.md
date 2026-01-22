# AI Resume Analyzer & Job Match Scorer

A full-stack web application that analyzes resumes and job descriptions using NLP embeddings to compute a semantic match score and provide actionable feedback.

## Features
- Resume PDF upload
- Job description analysis
- Semantic similarity scoring using AI embeddings
- REST API built with FastAPI
- Simple frontend interface

## Tech Stack
- Python
- FastAPI
- OpenAI API
- scikit-learn
- HTML, JavaScript

## Project Structure
ai-resume-matcher/
├── backend/
│   ├── main.py
│   ├── resume_parser.py
│   ├── matcher.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── app.js
├── .gitignore
└── README.md
## Setup Instructions
1. Clone the repository
2. Set the OpenAI API key as an environment variable
3. Install backend dependencies
4. Run the FastAPI backend server
5. Open the frontend in a web browser

## Future Improvements
- AI-generated resume improvement suggestions
- Skill gap and keyword visualization
- User authentication and saved analyses
- Cloud deployment for public access
