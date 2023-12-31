from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True) # db_index makes search the field quicker

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    
    # def save(self, *args, **kwargs): 
    #     self.slug = slugify(self.title) #this will create a slug based on the title 
    #     super().save(*args, **kwargs)
        
    
    
    def __str__(self):
        return f"{self.title}"