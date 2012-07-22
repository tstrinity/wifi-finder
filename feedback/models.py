#coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Feedback(models.Model):
    """
    feedback model, ordering set to time desc
    default table name changed to 'feedbacks'
    """
    class Meta:
        ordering = ['-time']
        db_table = 'feedbacks'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    email   = models.EmailField(verbose_name= _('Email'))
    type    = models.CharField(choices=settings.FEEDBACK_CHOICES, max_length=100, verbose_name=_('Type'))
    message = models.TextField(verbose_name=_('Message'))
    time    = models.DateTimeField(auto_now_add=True, verbose_name=_('Time'))

    def __unicode__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('admin:view-feedback', args=[self.id])
