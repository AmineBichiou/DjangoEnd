from django.db import models

class Skills(models.Model):
 nom = models.CharField(max_length=100)
 niveau = models.IntegerField()
 formation = models.CharField(max_length=100)
 dateS = models.DateField()
 language = models.ForeignKey('Language', on_delete=models.CASCADE,)
def __str__(self) -> str:
    return self.nom
class Language(models.Model):
    language = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    def __str__(self) -> str:
        return self.language
class diploma(models.Model):
 MyEducation = models.CharField(max_length=100)
 MyExperience = models.CharField(max_length=100)
 dateD = models.DateField()
class Internships(models.Model):
 namesociete = models.CharField(max_length=100)
 projet = models.CharField(max_length=100)
 dateI = models.DateField()