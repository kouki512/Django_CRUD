from django.db import models

# class SampleModel (models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()
    # Create your models here.

CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他')) # 連想配列やenumのようなもの

class Book(models.Model):
    title = models.CharField(max_length=100) # railsでいうとstring型
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )
    
    def __str__(self):
        return self.title

