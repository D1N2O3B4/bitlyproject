from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name} |{self.url} |{self.clicks}"
    
    def click(self)-> str:
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)