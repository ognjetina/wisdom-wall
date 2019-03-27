from django.db import models


class Wisdom(models.Model):
    words_of_wisdom = models.CharField(max_length=255)
    wisdom_origin = models.CharField(max_length=120)
    wisdom_occurrence_time = models.DateField(auto_now_add=True, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return 'Wisdom: ' + self.words_of_wisdom
