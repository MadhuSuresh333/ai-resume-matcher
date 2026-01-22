import openai
from sklearn.metrics.pairwise import cosine_similarity
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response["data"][0]["embedding"]

def match_resume_to_job(resume_text, job_text):
    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_text)

    score = cosine_similarity([resume_emb], [job_emb])[0][0]
    return round(score * 100, 2)
