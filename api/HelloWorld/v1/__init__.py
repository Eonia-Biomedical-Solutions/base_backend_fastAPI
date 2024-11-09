from fastapi import APIRouter

from .routes import hello_world_router

v1_subrouter = APIRouter(prefix="/v1")
v1_subrouter.include_router(hello_world_router,
                          prefix="/hello_world",
                          tags=["hello world"])


__all__ = ["v1_subrouter"]
