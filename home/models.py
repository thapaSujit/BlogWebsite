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
    
    def save(self, *args, **kwargs):
        # Calculate the approximate time required to read the content
        word_count = len(self.content.split())
        average_reading_speed = 200  # Assuming an average reading speed of 200 words per minute
        minutes_required = word_count / average_reading_speed

        # Round up to the nearest minute
        self.approx_time = str(round(minutes_required))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title