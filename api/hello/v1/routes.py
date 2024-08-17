from fastapi import APIRouter
from .request import SayNameRequest
from .response import SayNameResponse

hello_world_router = APIRouter()


@hello_world_router.get('/')
async def helloworld():

    response = 'Hello World!'

    return response


@hello_world_router.post('/my_name')
async def say_my_name(request: SayNameRequest) -> SayNameResponse:

    data: dict = request.model_validate(request).model_dump()

    msg: str = f"Hello {data['name']}"

    return SayNameResponse.model_validate({'msg': msg})
