from pydantic import BaseModel

class NotificationRequest(BaseModel):
    user_id: str
    type: str
    message: str
