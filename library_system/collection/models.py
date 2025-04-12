from django.db import models

# Create your models here.

class author(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    bio= models.TextField()
    
    def __str__(self):
        return self.name
    

class book(models.Model):
    title= models.CharField(max_length=50)
    genre= models.CharField(max_length=50)
    published_date= models.DateField()
    author= models.ForeignKey(author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class borrowRecord(models.Model):
    borrow_name= models.CharField(max_length=50)
    book= models.ForeignKey(book, on_delete=models.CASCADE)
    borrow_date= models.DateField()
    return_date= models.DateField()
    
    def __str__(self):
        return self.borrow_name or "No Name"
