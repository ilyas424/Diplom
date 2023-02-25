import db
import models

values = [
    models.TicketPriority(title="very low"),
    models.TicketPriority(title="low"),
    models.TicketPriority(title="medium"),
    models.TicketPriority(title="high"),
    models.TicketPriority(title="critical"),
    models.TicketStatus(title="ToDo"),
    models.TicketStatus(title="In Progress"),
    models.TicketStatus(title="Done"),
    models.TicketStatus(title="Closed"),
    models.TicketType(title="Task"),
    models.TicketType(title="Subtask"),
    models.TicketType(title="Epic"),
    models.TicketType(title="Bug"),
    models.TicketType(title="Story")
]

for value in values:
    try:
        session = db.SessionLocal()
        session.add(value)
        session.commit()
    except Exception as e:
        pass
