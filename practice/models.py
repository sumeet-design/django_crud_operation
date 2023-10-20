from django.db import models

# Create your models here.
class studentDetails(models.Model):
    name = models.CharField(max_length=255)
    standard = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=11)

    def __str__(self) -> str:
        return self.name