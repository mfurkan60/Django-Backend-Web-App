from django.db import models
from datetime import datetime

# Create your models here.
class Todos(models.Model):
    ## todonun başlığı,açıklaması,bittip bitmediği defoult olarak true al ve 
    ##oluşturma tarihi
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=True)
    finished  = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        ## bu fonksiyon admin kısmında başlığı dönderdi
        return self.title
