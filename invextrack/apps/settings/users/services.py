from .models import User

def create_user(username, password, email):
    user = User.objects.create_user(username=username, password=password, email=email)
    return user

def assign_role(user, role):
    user.groups.add(role)
    user.save()
    return user