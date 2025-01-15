import csv
from scheduler.models import Member
from django.contrib.auth.models import User
from decouple import config

def run():
    with open("hidden/AY24_25 Members Details.csv", 'r') as file:
        reader = csv.DictReader(file)
        print("File Opened")

        #Reset Member and User Table
        Member.objects.all().delete()
        User.objects.all().delete()

        #Create default user and superuser (REMEMBER TO UPDATE .env FILE)
        user = User.objects.create_user(
            username=config("DEFAULTUSERNAME"),
            password=config("DEFAULTUSERPASS")
            )
        user.first_name = "Member Account"
        user.save()

        superuser = User.objects.create_superuser(
            username=config("SUPERUSERNAME"),
            password=config("SUPERUSERPASS"),
            email='hallonejamband@gmail.com'
            )
        superuser.first_name = "CoChair Account"
        superuser.save()