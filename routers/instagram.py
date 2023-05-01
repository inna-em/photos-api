from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}

# @router.get("/getPhotos")
# async def get_photos(username: str = Query(..., description="Instagram username"),
#                       max_count: int = Query(10, gt=0, le=100, description="Maximum number of photos to return")):
#     # TODO: Implement logic to retrieve photos for the given username
#     # For now, we'll just return an empty list
#     urls = []
#     response = {"urls": urls}
#     return response


# @router.post("/postPhotos")
# async def post_photos(photos: list[UploadFile] = File(..., description="List of photos to post"),
#                        caption: str = "", description="Caption for the post"):
#     # TODO: Implement logic to post the photos with the given caption
#     # For now, we'll just return an empty string as the post URL
#     post_url = ""
#     response = {"postURL": post_url}
#     return response