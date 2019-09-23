from django.db import models

class book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    notes=models.TextField()
    books=models.ManyToManyField(book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Movie(models.Model):
    # fields removed for brevity
    def __repr__(self):
        return f"<book object: {self.title} ({self.desc})>"
