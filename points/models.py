#coding: utf-8

from django.forms.widgets import Select
from django.db import models
from providers.models import Provider
from django import forms

#Model for access point
class Point(models.Model):

    SIGNAL_QUALITY_CHOISES = (
        (1, u'Плохое'),
        (2, u'Жить можно'),
        (3, u'Хорошее'),
        (4, u'Отличное'),
    )

    name = models.CharField(u'Название', max_length=50)
    coordinate_latitude = models.DecimalField(u'Широта',decimal_places=20, max_digits=30)
    coordinate_longitude = models.DecimalField(u'Долгота', decimal_places=20, max_digits=30)
    average_signal = models.IntegerField(u'Качество сигнала', choices=SIGNAL_QUALITY_CHOISES)
    added_on = models.DateTimeField(auto_now=True)
    additional_info = models.CharField(u'Дополнительная информация', max_length=200)
    provider = models.ForeignKey(Provider, verbose_name=u'Провайдер')

    def __unicode__(self):
        return self.name

    #using custom table name
    class Meta:
        db_table = 'points'


#form for adding a new point
class PointAddForm(forms.ModelForm):
    name = forms.CharField(label=u'Название', min_length=2,max_length=30,required=True, error_messages={
        'required' : u'Введите название точки доступа',
        'min_length' : u'Название точки должно состоять из не мение 2 символов',
        'max_length' : u'Название точки должно состоять из не более 30 символов'
    })
    average_signal = forms.IntegerField(required = True, label=u'Качество сигнала',
        widget=Select(choices=Point.SIGNAL_QUALITY_CHOISES),
        error_messages={'required' : u'Укажите качество сигнала' })
    additional_info = forms.CharField(required= False, label=u'Дополнительная информация')
    provider = forms.ModelChoiceField(required=True,
        label=u'Провайдер',queryset=Provider.objects.all(),
        error_messages={'required' : u'Вы не указали провайдера'})
    coordinate_latitude = forms.DecimalField(required=True, label=u'Широта',
        error_messages={'required' : u'Введите широту или поставьте маркер на карте' })
    coordinate_longitude = forms.DecimalField(required=True, label=u'Долгота',
        error_messages={'required' : u'Введите долготу или поставьте маркер на карте' })

    class Meta:
        model = Point