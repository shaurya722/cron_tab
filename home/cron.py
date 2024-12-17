

from cron_tab import settings
from home.models import Test,Document
from datetime import datetime
from django.core.mail import send_mail



def my_scheduled_job():

    Test.objects.create(name='test')
  

def document_expired_check():
    # Your email sending logic
        subject = "Scheduled Email"
        message = f"This is a test email sent at {datetime.now()}."
        recipient_list = ["joshishaurya31@gmail.com"]  

        # Send email using Django's built-in send_mail function
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, 
            recipient_list,
        )

        print(f"Email sent at {datetime.now()}")