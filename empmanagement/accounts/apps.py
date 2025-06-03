from django.apps import AppConfig
# from django.contrib.auth.models import User
# import os


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

# class YourAppNameConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'accounts'  # <-- replace with your app's name

#     def ready(self):
#         if os.environ.get('CREATE_SUPERUSER') == 'True':
#             username = 'Puushkar_Dhharaap'
#             email = 'vaishnavichandgude0411@gmail.com'
#             password = 'Puushkar@#987'
#             if not User.objects.filter(username=username).exists():
#                 print("Creating superuser...")
#                 User.objects.create_superuser(username=username, email=email, password=password)
