from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from schema.sample_object import SampleObject as SampleObjectSchema
from model.sample_object import SampleObject as SampleObjectModel

logger = Logger.get_logger(__name__)

class SampleRepository():
    def __init__(self, db_session: Session = Depends(get_db_session)) -> None:
        self.db = db_session

    def get_by_id(self, id):
        logger.debug('Getting item {} from db'.format(id))
        return self.db.query(SampleObjectModel).get({'id': id})

    def insert(self, item: SampleObjectSchema):
        logger.debug('Insert item {}'.format(str(item)))
        db_item = SampleObjectModel(id=item.id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
