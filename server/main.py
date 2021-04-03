# just load all the controllers
import controller

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_router_controller import Controller, ControllersTags

from utils.config import Config
from utils.middleware import LogIncomingRequest, exception_handler, validation_exception_handler

#########################################
#### Configure the main application #####
#########################################
app = FastAPI(
    title='{}'.format(Config.read('app', 'name')),
    description='This is a very fancy project, with auto docs for the API and everything',
    version='0.0.1',
    docs_url=Config.read('app', 'api-docs.path'),
    openapi_tags=ControllersTags)

# configuring handler for validation error in order to format the response
app.exception_handler(RequestValidationError)(validation_exception_handler)

# configuring handler for generic error in order to format the response
app.exception_handler(Exception)(exception_handler)

# add middleware to process the request before it is taken by the router func
app.add_middleware(LogIncomingRequest)

#########################################
#### Configure all the implemented  #####
####  controllers in the main app   #####
#########################################
for router in Controller.routers():
    app.include_router(router)
