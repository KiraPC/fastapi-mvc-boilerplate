import os
from pathlib import Path
from configparser import ConfigParser

this_dir = Path(__file__).parent
conf_dir = this_dir / 'properties.ini'

parser = ConfigParser(os.environ)
parser.read(conf_dir, encoding="utf8")

class Config():
    @staticmethod
    def read(section, property, default=None):
        return parser.get(section, property) or default
