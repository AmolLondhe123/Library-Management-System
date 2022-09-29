from django.db import models

# Create your models here.

class Admin(models.Model):
    Uname=models.CharField(max_length=200,primary_key=True)
    email=models.EmailField(null=False,unique=True)
    password=models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return self.Uname
    
    
class Library(models.Model):
    book_title = models.CharField(max_length=200,null=False)
    book_author = models.CharField(max_length=100,null=False)
    book_pages = models.IntegerField()
    def __str__(self):
        return self.book_title

