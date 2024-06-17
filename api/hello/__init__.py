from fastapi import APIRouter

from .helloworld import hello_world

sub_router = APIRouter()
sub_router.include_router(
    hello_world
)
