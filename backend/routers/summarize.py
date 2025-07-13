from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/summarize",
    tags=["summarize"]
)

class SummaryRequest(BaseModel):
    text: str

class TermsReport(BaseModel):
    summary: str

class PrivacyReport(BaseModel):
    summary: str

@router.post("/terms", response_model=TermsReport)
async def get_users(req: SummaryRequest):
    if not req or not req.text:
        raise HTTPException(status_code=422, detail="Missing 'text' parameter")
    else:
        # call llm service
        return TermsReport(summary="This is a mock summary of the terms")

@router.post("/privacy", response_model=PrivacyReport)
async def get_user(req: SummaryRequest):
    if not req and not req.text:
        raise HTTPException(status_code=422, detail="Missing 'text' parameter")
    else:
        # call llm service
        return PrivacyReport(summary="This is a mock summary of the privacy policy")
