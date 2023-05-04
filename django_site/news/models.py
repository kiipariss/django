from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Stata')
    date = models.DateTimeField('Data')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

