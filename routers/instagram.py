from fastapi import APIRouter, Query, File, UploadFile
from dependencies import get_photo_urls, upload_photos

router = APIRouter()

# An endpoint to test the app is responsive
@router.get("/")
async def root():
    return {"message": "Hello World"}

# TODO fields validation
@router.get("/getPhotos")
async def get_photos(username: str = Query(..., description="Instagram username"),
                     max_count: int = Query(10, gt=0, le=100, description="Maximum number of photos to return")):
    urls = get_photo_urls(username, max_count)
    response = {"urls": urls}
    return response


@router.post("/postPhotos")
async def post_photos(photos: list[UploadFile] = File(..., description="List of photos to post"),
                      caption: str = ""):
    post_url = upload_photos(photos, caption)
    response = {"postURL": post_url}
    return response
