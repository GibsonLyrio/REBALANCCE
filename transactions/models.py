from django.db import models

# Create your models here.
class Transactions(models.Model):
  type = models.BooleanField()
  value = models.FloatField()
  description = models.CharField(max_length=30)

  def __str__(self) -> str:
    return self.description
