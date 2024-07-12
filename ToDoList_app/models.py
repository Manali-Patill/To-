from django.db import models

# Create your models here.
class todoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)  # Add this line
    deleted_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return self.title
