from pydantic import BaseModel

class SampleObject(BaseModel):
    id: str

    class Config:
        orm_mode = True
