from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)
    #approx_time = models.PositiveIntegerField(blank=True, null=True)

    def get_read_time(self):
        from html import unescape
        from django.utils.html import strip_tags
        
        string = self.title + unescape(strip_tags(self.content))
        total_words = len((string).split())

        return round(total_words / 200)

    def __str__(self):
        return self.title