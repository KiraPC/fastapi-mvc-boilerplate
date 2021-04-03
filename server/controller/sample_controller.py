from fastapi.responses import JSONResponse
from fastapi_router_controller import Controller
from fastapi import APIRouter, status, Query, Body, Depends

from utils.logger import Logger
from schema.sample_object import SampleObject
from service.sample_service import SampleService

router = APIRouter(prefix='/sample-controller')
controller = Controller(router, openapi_tag={
    'name': 'sample-controller',
})

logger = Logger.get_logger(__name__)

@controller.use()
@controller.resource()
class SampleController():
    def __init__(self, service: SampleService = Depends()) -> None:
        self.service = service

    @controller.route.get(
        '', 
        tags=['sample-controller'], 
        summary='Get Object from DB', 
        response_model=SampleObject)
    def get_sample_object(
        self,
        id: str = Query(
            ...,
            title="itemId",
            description="The id of the item to get")):
        try:
            item = self.service.get_by_id(id)

            if item is None:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    content={ 'error': 'Content not found on DB' }
                )
    
            return item
        except Exception as error:
            logger.error('Error getting item: {}'.format(error))
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                content={ 'error': 'An error occured' }
            )

    @controller.route.post(
        '',
        tags=['sample-controller'], 
        summary='Intert a new Item on DB.', 
        status_code=201,
        response_description='The item was created on DB. No body is provided')
    def add_sample_object(
        self,
        sample_object: SampleObject = Body(
            ..., 
            title="Item", 
            description="The item object to store")):
        try:
            self.service.insert(sample_object)
            return JSONResponse(
                status_code=status.HTTP_201_CREATED
            )
        except Exception as error:
            logger.error('Error inserting item: {}'.format(error))
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                content={ 'error': 'An error occured' }
            )
