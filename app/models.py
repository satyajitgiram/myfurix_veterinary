from django.db import models

class Testimonial(models.Model):
    STAR_CHOICES = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    )

    star_rating = models.IntegerField(choices=STAR_CHOICES)
    quote_text = models.TextField()
    client_name = models.CharField(max_length=100)
    client_profession = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='testimonial_images/')

    def __str__(self):
        return self.client_name
