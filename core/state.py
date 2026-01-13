from dataclasses import dataclass
from datetime import datetime
from sqlite3.dbapi2 import Timestamp

@dataclass
class Volstate:
    asset: str
    timestamp: datetime

    level : float
    curvature : float 
    skew : float 
