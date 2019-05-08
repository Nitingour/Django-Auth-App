from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField(upload_to="images/")
    upload_date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=50)
