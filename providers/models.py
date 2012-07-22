#coding: utf-8

from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

class Provider(models.Model):
    """
    provider model for providers
    table name set to 'providers'
    uploaded logo goes to media/year/month/day
    """
    name = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='%Y/%m/%d')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'providers'
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')

class ProviderForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30, required=True, error_messages={
        'required' : _('Write provider name'),
        'max_length' : _('Not more than 50 symbols')
    })
    site = name = forms.CharField(label='Site', max_length=50, required=True, error_messages={
        'required' : _('Write provider web site'),
        'max_length' : _('Not more than 50 symbols')
    })
    class Meta:
        model = Provider
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')