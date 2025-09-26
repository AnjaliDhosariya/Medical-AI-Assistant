from fastapi import APIRouter,File, UploadFile
from typing import List
from modules.load_vectorstores import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger

router = APIRouter()
@router.post("/upload_pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    try: 
        logger.info("Received files for upload")
        load_vectorstore(files)
        logger.info("Files uploaded to vector store successfully")
        return {"message": "Files processed and vectorstore updates successfully"}
    except Exception as e:
        logger.exception("Error occured during file upload")
        return JSONResponse(status_code=500, content={"message": str(e)})