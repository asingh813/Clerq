from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from analyze_contract import analyze_contract_text
from utils.file_parser import extract_text_from_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/upload/")
async def upload_contract(file: UploadFile = File(...)):
    text = await extract_text_from_file(file)
    analysis = analyze_contract_text(text)
    return {"analysis": analysis}
