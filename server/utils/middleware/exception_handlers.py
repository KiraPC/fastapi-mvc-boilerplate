from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from utils.logger import Logger
logger = Logger.get_logger(__name__)

def validation_exception_handler(_: Request, exc: RequestValidationError):
    error = exc.errors()[0]
    message = 'Validation error: {} {}'.format('.'.join(error['loc']), error['msg'])
    return JSONResponse(status_code=400, content={ 'error': message })


async def exception_handler(req: Request, exc: Exception):
    func_handler = req.state.func_name
    logger.error('An error occured during {} handling. Error: {}'.format(func_handler, exc))
    return JSONResponse(status_code=500, content={ 'error': 'Internal Server Error' })
