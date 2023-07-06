from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PageInfo(BaseModel):
    url: str
    body: str


@app.post("/analyze_page")
def sendpage(page_info: PageInfo):
    return {"reply": "Analysis Complete!"}
