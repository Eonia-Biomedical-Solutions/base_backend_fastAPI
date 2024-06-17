from fastapi import APIRouter

from .hello import sub_router

router = APIRouter()


router.include_router(sub_router)

__all__ = ["router"]