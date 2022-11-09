from django.db import models


class Todo(models.Model):

    Title = models.CharField(max_length=200, blank=100)
    Desc = models.TextField(blank=True)
    Date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.Title
