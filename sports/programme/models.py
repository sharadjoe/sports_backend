from django.db import models


class Programme(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name