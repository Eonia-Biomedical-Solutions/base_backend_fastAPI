from fastapi import APIRouter

from .routes import hello_world_router

sub_router = APIRouter(prefix="/v1")
sub_router.include_router(hello_world_router,
                          prefix="/hello_world",
                          tags=["hello world"])


__all__ = ["sub_router"]
