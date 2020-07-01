from django.db import models

# Create your models here.
# URL, NAME
class Bookmark(models.Model):
    site_name = models.CharField(max_length=130)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name +':' + self.url