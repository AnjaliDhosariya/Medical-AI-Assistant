import os
import shutil
from fastapi import UploadFile
import tempfile

UPLOAD_DTR = "./uploaded_docs"

def save_uploaded_files(uploaded_files: list[UploadFile]) -> list[str]:
    os.mkdirs(UPLOAD_DIR, exist_ok=True)
    file_path=[]
    for file in uploaded_files:
        temp_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        filepath.append(temp_path)
    return file_path
    