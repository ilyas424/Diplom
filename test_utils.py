from sqlalchemy.orm import Session

from utils import get_ticket_priorities_from_db

def test():
    assert get_ticket_priorities_from_db(Session)  == ()



