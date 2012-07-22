from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangosphinx import SphinxSearch

class Post(models.Model):
    """
    model for posts
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        db_table = 'posts'

    #sphinx search data
    search = SphinxSearch(
        index = 'posts',
        weights = {
            'title': 90,
            'content' : 100,
            'created_at' : 10,
        }
    )
