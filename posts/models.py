from django.db import models
from djangosphinx import SphinxSearch

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'posts'

    search = SphinxSearch(
        index = 'posts',
        weights = {
            'title': 90,
            'content' : 100,
            'created_at' : 10,
        }
    )
