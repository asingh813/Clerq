import fitz  # PyMuPDF
import docx2txt

async def extract_text_from_file(file):
    if file.filename.endswith(".pdf"):
        pdf = fitz.open(stream=await file.read(), filetype="pdf")
        return "".join([page.get_text() for page in pdf])
    elif file.filename.endswith(".docx"):
        return docx2txt.process(file.file)
    return "Unsupported file type"
