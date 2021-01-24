from django.db import models

# Create your models here.
class countries(models.Model):
    room_num = models.TextField()
    check_in = models.TextField()
    check_out = models.TextField()
    grade = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
