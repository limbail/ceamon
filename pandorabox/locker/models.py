from django.db import models as m
from django.core.urlresolvers import reverse
 
class locker(m.Model):
    title = m.CharField(max_length=200)
    username = m.CharField(max_length=200,
        unique=True,
        blank=True)
    password = m.CharField(max_length=200)
    url = m.URLField(max_length=500,
        blank=True,
        verbose_name='Site URL',
        default='http://temporal.corp')
    notes = m.TextField(
        max_length=500,
        blank=True,
        help_text='Any extra notes')
    created_at = m.DateTimeField(auto_now_add=True, editable=False)
    updated_at = m.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self):
        return reverse('locker-detail', kwargs={'pk': self.pk}) 
