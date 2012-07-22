#coding: utf-8

from django.forms.widgets import Select
from django.db import models
from providers.models import Provider
from django import forms
from django.utils.translation import ugettext_lazy as _


class Point(models.Model):

    """
    Point model
    db table name set to 'points'
    """

    SIGNAL_QUALITY_CHOICES = (
        (1, _('Bad')),
        (2, _('Average')),
        (3, _('Good')),
        (4, _('Excellent')),
    )

    name = models.CharField(_('Name'), max_length=50)
    coordinate_latitude = models.DecimalField(_('Latitude'),decimal_places=20, max_digits=30)
    coordinate_longitude = models.DecimalField(_('Longtitude'), decimal_places=20, max_digits=30)
    average_signal = models.IntegerField(_('Signal quality'), choices=SIGNAL_QUALITY_CHOICES)
    added_on = models.DateTimeField(auto_now=True)
    additional_info = models.CharField(_('Additional info'), max_length=200)
    provider = models.ForeignKey(Provider, verbose_name=_('Provider'))

    def __unicode__(self):
        return self.name

    #using custom table name
    class Meta:
        db_table = 'points'
        verbose_name = _('Point')
        verbose_name_plural = _('Points')


#form for adding a new point
class PointAddForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), min_length=2,max_length=30,required=True, error_messages={
        'required' : _('Write access point name'),
        'min_length' : _('Minimum length is 2 characters'),
        'max_length' : _('Maximum length is 30 characters')
    })
    average_signal = forms.IntegerField(required = True, label=_('Signal quality'),
        widget=Select(choices=Point.SIGNAL_QUALITY_CHOICES),
        error_messages={'required' : _('Please, select signal quality') })
    additional_info = forms.CharField(required= False, label=_('Additional info'))
    provider = forms.ModelChoiceField(required=True,
        label=_('Provider'),queryset=Provider.objects.all(),
        error_messages={'required' : _('Please, select provider')})
    coordinate_latitude = forms.DecimalField(required=True, label= _('Latitude'),
        error_messages={'required' : _('Please enter latitude or set point location on map') })
    coordinate_longitude = forms.DecimalField(required=True, label=_('Longtitude'),
        error_messages={'required' : _('Please enter longtitude or set point location on map') })

    class Meta:
        model = Point
        verbose_name = _('Point')
        verbose_name_plural = _('Points')
