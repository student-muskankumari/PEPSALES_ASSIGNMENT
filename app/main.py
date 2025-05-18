from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal
from .notification_sender import send_email, send_sms

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notifications")
def send_notification(request: schemas.NotificationRequest, db: Session = Depends(get_db)):
    notif = models.Notification(**request.dict())
    db.add(notif)
    db.commit()
    db.refresh(notif)

    try:
        if notif.type == "email":
            send_email(notif.user_id, notif.message)
        elif notif.type == "sms":
            send_sms(notif.user_id, notif.message)
        notif.status = "sent"
    except Exception:
        notif.status = "failed"

    db.commit()
    return {"message": notif.status, "id": notif.id}

@app.get("/users/{id}/notifications")
def get_user_notifications(id: str, db: Session = Depends(get_db)):
    return db.query(models.Notification).filter(models.Notification.user_id == id).all()
