import db
import models

values = [
    models.TicketPriority(name="very low"),
    models.TicketPriority(name="low"),
    models.TicketPriority(name="medium"),
    models.TicketPriority(name="high"),
    models.TicketPriority(name="critical"),
    models.TicketStatus(name="ToDo"),
    models.TicketStatus(name="In Progress"),
    models.TicketStatus(name="Done"),
    models.TicketStatus(name="Closed"),
    models.TicketType(name="Task"),
    models.TicketType(name="Subtask"),
    models.TicketType(name="Epic"),
    models.TicketType(name="Bug"),
    models.TicketType(name="Story")
]

for value in values:
    try:
        session = db.SessionLocal()
        session.add(value)
        session.commit()
    except Exception as e:
        pass
