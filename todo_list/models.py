from django.db import models

# Create your models here. 
# (11:05)
class List(models.Model):
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item + ' | ' + str(self.completed)
    
    