from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Report(BaseModel):
    content: str





@app.post("/classify")
def classify_report(report: Report):
    return {"Mach deinen scheiß selber": report}
