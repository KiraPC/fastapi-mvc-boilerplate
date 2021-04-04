from fastapi import Request
from schema.errors import Errors
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from utils.logger import Logger
logger = Logger.get_logger(__name__)

def validation_exception_handler(_: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    message = 'Validation error: {} {}'.format('.'.join(error['loc']), error['msg'])
    return Errors.HTTP_400_BAD_REQUEST(message)


async def exception_handler(req: Request, exc: Exception):
    func_handler = req.state.func_name
    logger.error('An error occured during {} handling. Error: {}'.format(func_handler, exc))
    return Errors.HTTP_500_INTERNAL_SERVER_ERROR
