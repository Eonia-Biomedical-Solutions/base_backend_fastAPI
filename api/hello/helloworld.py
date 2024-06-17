from fastapi import APIRouter

hello_world = APIRouter()


@hello_world.get('/')
async def helloworld():

    response = 'Hello World!'

    return response
