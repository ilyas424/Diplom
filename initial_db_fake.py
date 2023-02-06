import db
import models

values = [
    models.User(name="Пирожков Артур"),
    models.User(name="Никита Никитов"),
    models.User(name="Адрей Андреев"),
    models.Ticket(description="super", priority_id=1, type_id=1, status_id=1, reporter_id=1, assignee_id=1),
    models.TicketComment(ticket_id=1, text="super task", author_id=1)
]

for value in values:
    try:
        session = db.SessionLocal()
        session.add(value)
        session.commit()
    except Exception as e:
        pass
