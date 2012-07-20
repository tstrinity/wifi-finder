from django.db import models
from django.forms.models import ModelForm

class Provider(models.Model):
    '''
    provider model for providers
    table name set to 'providers'
    uploaded logo goes to media/y/m/d
    '''
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='%Y/%m/%d')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'providers'

class ProviderForm(ModelForm):
    class Meta:
        model = Provider