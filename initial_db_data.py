import db
import models

ticket_priorities = [
    models.TicketPriority(name = "very low1"),
    models.TicketPriority(name = "low"),
    models.TicketPriority(name = "medium"),
    models.TicketPriority(name = "high"),
    models.TicketPriority(name = "critical")
]

for ticket_priority in ticket_priorities:
    try:
        session = db.SessionLocal()
        session.add(ticket_priority)
        session.commit()
    except Exception as e:
        pass
