from django.db import models

class DipQ(models.Model):
    diplome = models.TextField(max_length=100)
    qualification = models.TextField(max_length=100)
    def __str__(self) -> str:
        return self.diplome