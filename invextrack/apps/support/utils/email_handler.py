from django.core.mail import send_mail

def send_support_email(subject, message, recipient_list):
    send_mail(subject, message, 'support@example.com', recipient_list)