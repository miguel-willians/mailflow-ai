from PyPDF2 import PdfReader
from fastapi import UploadFile
import io

def read_email_file(file: UploadFile) -> str:
    """
    Recebe um arquivo enviado via FastAPI (UploadFile)
    e retorna o texto extraído.
    
    Suporta arquivos .txt e .pdf.
    """
    filename = str(file.filename).lower()  # garante que não seja None

    if filename.endswith(".txt"):
        # Lê diretamente o conteúdo
        content = file.file.read().decode("utf-8")
        return content.strip()

    elif filename.endswith(".pdf"):
        # Lê PDF usando PyPDF2
        pdf_bytes = file.file.read()
        reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()

    else:
        raise ValueError("Formato de arquivo não suportado. Use .txt ou .pdf")
