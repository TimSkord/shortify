from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from db.database import get_db
from db.models import URL
from schemas import URLCreate, URLResponse
from utils import create_short_url

router = APIRouter(
    prefix='',
)


@router.get("/", response_model=List[URLResponse])
async def list_all_urls(session: Session = Depends(get_db)):
    urls = session.query(URL).all()
    return urls


@router.post("/", response_model=URLResponse, status_code=201)
async def shorten_url(url: URLCreate, session: Session = Depends(get_db)):
    short_url = create_short_url(url.full_url)

    existing_url = session.query(URL).filter(URL.full_url == url.full_url).first()
    if existing_url:
        return existing_url

    db_url = URL(full_url=url.full_url, short_url=short_url)
    session.add(db_url)
    session.commit()
    session.refresh(db_url)
    return db_url


@router.get("/{short_url}/", response_class=RedirectResponse)
async def redirect_to_full_url(short_url: str, session: Session = Depends(get_db)):
    db_url = session.query(URL).filter(URL.short_url == short_url).first()

    if db_url is None:
        raise HTTPException(status_code=404)

    return RedirectResponse(url=db_url.full_url)


@router.delete("/{short_url}/", status_code=204)
async def delete_url(short_url: str, session: Session = Depends(get_db)):
    db_url = session.query(URL).filter(URL.short_url == short_url).first()

    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")

    session.delete(db_url)
    session.commit()

    return {"message": "URL deleted successfully"}
