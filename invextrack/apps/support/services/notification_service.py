from django.core.mail import send_mail

def send_notification(email, subject, message):
    send_mail(subject, message, 'from@example.com', [email])