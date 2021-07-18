from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Dict, Any

import jwt

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


app = FastAPI()


JWT_SIGNING_KEY = "secret"


def jwt_middleware(auth: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    try:
        return jwt.decode(auth.credentials, JWT_SIGNING_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token")


class Report(BaseModel):
    content: str


@app.post("/classify")
def classify_report(report: Report, claims: Dict[str, Any] = Depends(jwt_middleware)):
    return {"Mach deinen scheiß selber": report, "claims": claims}
