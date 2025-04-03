from pydantic import BaseModel, EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import os
from dotenv import load_dotenv

load_dotenv()

class EmailSchema(BaseModel):
    email: EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=465,
    MAIL_SERVER="smtp.meta.ua",
    MAIL_FROM_NAME="Rest API Service",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def send_verification_email(email: str, token: str):
    message = MessageSchema(
        subject="Verify your email",
        recipients=[email],
        body=f"Click the link to verify your email: http://127.0.0.1:8000/auth/verify-email?token={token}",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
