import os
from fastapi_router_controller import ControllerLoader

this_dir = os.path.dirname(__file__)

ControllerLoader.load(this_dir, __package__)
