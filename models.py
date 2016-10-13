
from django.db import models

class PrimitiveWikimediaEntry ( models.Model ):

    creation_date = models.DateTimeField ( auto_now_add=True )
    orig_url = models.CharField ( max_length=128 )
    url1 = models.CharField ( max_length=128 )
    url2 = models.CharField ( max_length=128 )
    url3 = models.CharField ( max_length=128 )

    class Meta:
        ordering = ['-creation_date']
        verbose_name = "Primitive Wikimedia Entry"
        verbose_name_plural = "Primitive Wikimedia Entries"

    def __str__ ( self ):
        return "[%s] Primitive Wikimedia Entry from %s" % ( self.creation_date.strftime ( '%Y%m%d' ), self.orig_url )

    def title ( self ):
        return self.creation_date.strftime ( "%B %-d, %Y" )
