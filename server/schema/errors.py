from fastapi import status
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

class ErrorModel(BaseModel):
    error: str = Field(..., description='The error message description')

class ErrorResponse(dict):
    def __init__(self, message):
        dict.__init__(self, error=message)

class Errors():
    HTTP_500_INTERNAL_SERVER_ERROR = JSONResponse(ErrorResponse('Internal Server Error'), status.HTTP_500_INTERNAL_SERVER_ERROR)
    HTTP_404_NOT_FOUND = JSONResponse(ErrorResponse('Content not found on DB'), status.HTTP_404_NOT_FOUND)
