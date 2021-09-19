from django.db import models

# Create your models here.
class User(models.Model):
    username = models.EmailField(primary_key=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.username

class Complaint(models.Model):
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.title