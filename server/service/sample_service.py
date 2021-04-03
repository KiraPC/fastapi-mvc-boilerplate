from fastapi import Depends

from utils.logger import Logger
from schema.sample_object import SampleObject
from repository.sample_repository import SampleRepository

logger = Logger.get_logger(__name__)

class SampleService():
    def __init__(self, repository: SampleRepository = Depends()) -> None:
        self.repository = repository

    def get_by_id(self, id):
        logger.debug('Getting item {} from db'.format(id))
        return self.repository.get_by_id(id)

    def insert(self, item: SampleObject):
        logger.debug('Insert item {}'.format(str(item)))
        self.repository.insert(item)
