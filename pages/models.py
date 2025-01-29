from django.db import models
from django.urls import reverse

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
    
    def get_absolute_url(self):
        return reverse('pages:review-detail', args=[str(self.id)])