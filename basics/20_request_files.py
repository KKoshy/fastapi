# Request Files
# Learn how to handle file uploads in FastAPI

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# TODO: Import File and UploadFile from fastapi
# Hint: from fastapi import FastAPI, File, UploadFile

# TODO: Create a POST endpoint at "/files/" that:
# 1. Accepts a file parameter as bytes using File()
# 2. Returns the file size in a dictionary
# 
# Hint: Use file: bytes = File() for the parameter
# Return: {"file_size": len(file)}
@app.post("/files/")
async def get_file_size(file: bytes = File()):
    return {"file_size": len(file)}

# TODO: Create a POST endpoint at "/uploadfile/" that:
# 1. Accepts a file parameter as UploadFile
# 2. Returns the filename in a dictionary
#
# Hint: Use file: UploadFile for the parameter (no = File() needed)
# Return: {"filename": file.filename}
@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    return {"filename": file.filename}
