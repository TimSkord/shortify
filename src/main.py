from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from router import router

app = FastAPI()
app.include_router(router)


@app.exception_handler(HTTPException)
async def url_not_found_exception_handler(request, exc):
    if exc.status_code == 404:
        return JSONResponse(status_code=404, content={"message": "URL not found"})
