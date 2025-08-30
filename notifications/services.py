from django.utils import timezone
from .models import Notification
from decouple import config
from twilio.rest import Client
from django.core.mail import send_mail


# Send Email via SendGrid
def send_email(notification: Notification):
    try:
       send_mail(
           subject="Kijani Kinga Alert",
           message=notification.message,
           from_email=config("SENDGRID_FROM_EMAIL"),
           recipient_list=[notification.recipient.email],
           fail_silently=False,
        )
       notification.status = "sent"
       notification.sent_at = timezone.now()
       notification.save()
    except Exception as e:
        notification.status = "failed"
        notification.save()
        print(f"Email failed: {e}")

# Twilio sender
def send_sms(notification: Notification):
    try:
        client = Client(config("TWILIO_SID"), config("TWILIO_AUTH_TOKEN"))
        client.messages.create(
            body=notification.message,
            from_=config("TWILIO_PHONE"),
            to=notification.recipient.userprofile.phone_number,
        )
        notification.status = "sent"
        notification.sent_at = timezone.now()
        notification.save()
    except Exception as e:
        notification.status = "failed"
        notification.save()
        print(f"SMS failed: {e}")