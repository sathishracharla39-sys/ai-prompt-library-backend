from django.db import models

class Prompt(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    complexity = models.IntegerField()

    def __str__(self):
        return self.title