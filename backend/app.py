from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from utils.file_reader import read_email_file
from gemini_ai import classify_and_respond

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_email/")
async def process_email(email_text: str = Form(...)):
    """
    Recebe email via formulário de texto
    """
    try:
        result = classify_and_respond(email_text)
        return result
    except ValueError as e:
        return {"error": str(e)}

@app.post("/process_email_file/")
async def process_email_file(file: UploadFile = File(...)):
    """
    Recebe email via upload de arquivo (.txt ou .pdf)
    """
    try:
        email_content = read_email_file(file)
    except ValueError as e:
        return {"error": str(e)}

    try:
        result = classify_and_respond(email_content)
        return result
    except ValueError as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
