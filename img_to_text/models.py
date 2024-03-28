from django.db import models


class Img2Text(models.Model):
    image = models.URLField()
    extracted_text  = models.TextField()

    def __str__(self) -> str:
        return f'{self.pk}'