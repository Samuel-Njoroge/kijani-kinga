from django.db.models.signals import post_save
from django.dispatch import receiver
from reports.models import Report
from .models import Notification
from .services import send_email, send_sms


@receiver(post_save, sender=Report)
def notify_on_report_update(sender, instance, created, **kwargs):
    if created:
        message = f"New report submitted: {instance.title}"
    elif instance.status == "verified":
        message = f"Report verified: {instance.title}"
    elif instance.status == "closed":
        message = f"Report closed"
    else:
        return
    
    notification = Notification.objects.create(
        recipient=instance.reporter,
        channel="email",
        message=message,
    )
    send_email(notification)