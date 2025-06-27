from django.db import models

class Rubric(models.Model):
    name= models.CharField(max_length=20)
class Rroduct(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    rubric = models.ForeignKey("Rubric", on_delete=models.CASCADE)