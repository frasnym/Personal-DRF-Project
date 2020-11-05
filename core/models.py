from django.db import models


class UserRegistration(models.Model):
    # ? Declare Account Status Value
    ACTIVE_ACCOUNTSTATUS = 1
    INACTIVE_ACCOUNTSTATUS = 0
    ACCOUNTSTATUS_CHOICES = (
        (ACTIVE_ACCOUNTSTATUS, "Active"),
        (INACTIVE_ACCOUNTSTATUS, "Inactive"),
    )

    username = models.TextField(max_length=20, unique=True)
    password = models.TextField(max_length=200)
    full_name = models.TextField(max_length=100)
    email_address = models.TextField(max_length=100, unique=True)
    phone_number = models.TextField(max_length=20, unique=True)
    current_address = models.TextField(max_length=200)
    account_status = models.IntegerField(
        choices=ACCOUNTSTATUS_CHOICES, default=ACTIVE_ACCOUNTSTATUS
    )

    def __str__(self):
        return self.username