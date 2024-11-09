from fastapi import APIRouter

from .HelloWorld import v1_HelloWorld

router = APIRouter()

router.include_router(v1_HelloWorld)


__all__ = ["router"]
