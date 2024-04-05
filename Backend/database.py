from tinydb import TinyDB
from dataclasses import dataclass, asdict
import datetime
from pathlib import Path

@dataclass
class logs:
    route_log: str
    date: str
    time: str

db = TinyDB(Path(__file__).parent.parent/ "Database" / "db.json")

def get_logs():
    return db.all()

def insert_log(route_log):
    time = datetime.datetime.now()
    log = logs(route_log, time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"))
    db.insert(asdict(log))