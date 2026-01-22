from fastapi import FastAPI, UploadFile, Form
from resume_parser import extract_text_from_pdf
from matcher import match_resume_to_job

app = FastAPI()

@app.post("/match")
async def match_resume(
    resume: UploadFile,
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume.file)
    score = match_resume_to_job(resume_text, job_description)

    return {
        "match_score": score,
        "description": "Higher score means better resume-job alignment"
    }
