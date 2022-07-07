from django.db import models

class Type(models.Model):
   title = models.CharField(max_length=40)

   def __str__(self):
      return self.title


   class Meta:
      ordering = ['title']

class Announcement(models.Model):
   title = models.CharField(max_length=40)
   description = models.TextField(null=True, blank=True)
   price = models.DecimalField(max_digits=11, decimal_places=2)
   type = models.ForeignKey(Type, on_delete=models.CASCADE)
   created_in = models.DateTimeField(auto_now_add=True)
   edited_in = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.title