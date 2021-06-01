from django.db import models
from django .contrib.auth.models import User
# Create your models here.

class Login(models.Model):
    class Meta:
        db_table ="login"

    USER_TYPE_CHOICES = (
        ('hod', 'Hod' ),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERTYPE = models.CharField(max_length=20,choices=USER_TYPE_CHOICES , null=False)
    def _str_(self):
        return f' {self.user.username} '
