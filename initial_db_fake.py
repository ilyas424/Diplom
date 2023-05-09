import db
import models

values = [
    models.User(name="Пирожков Артур", email="arthur@email.net"),
    models.User(name="Никита Никитов", email="nikita@internet.net"),
    models.User(name="Адрей Андреев", email="andry@google.ru"),
    models.Ticket(
        title="new tas to do",
        description="super",
        priority="high",
        reporter_email="arthur@email.net",
        assignee_email="arthur@email.net"
    ),
    models.TicketComment(ticket_id=1, text="super task", author_email="nikita@internet.net")
]

for value in values:
    try:
        session = db.SessionLocal()
        session.add(value)
        session.commit()
    except Exception as e:
        pass
