from django.db import models

class Collection (models.Model):

    name = models.CharField (max_length=256)

    def galleries (self, ignore=False):
        return self.gallery_set.filter (ignore=ignore)

    def __unicode__(self):
        return "%s" % self.name

class Gallery (models.Model):

    class Meta:

        verbose_name_plural = 'galleries'

    COLOR_CHOICES = (
        ('red', 'red'),
        ('green', 'green'),
        ('blue', 'blue')
    )

    color = models.CharField (max_length=5, choices=COLOR_CHOICES)

    TYPE_CHOICES = (
        ('figure', 'figure'),
        ('vehicle', 'vehicle')
    )

    type = models.CharField (max_length=7, choices=TYPE_CHOICES)

    collection = models.ForeignKey (Collection)
    name = models.CharField (max_length=256)
    url = models.URLField (max_length=256, verify_exists=False)
    ignore = models.BooleanField (default=False)

    def images (self, ignore=False):
        return self.image_set.filter (ignore=ignore)

    def __unicode__(self):
        return "%s" % self.name

class Image (models.Model):

    name = models.CharField (max_length=256)
    url = models.URLField (max_length=256, verify_exists=False)
    ignore = models.BooleanField (default=False)

    gallery = models.ForeignKey (Gallery)
    rate = models.DecimalField (max_digits=4, decimal_places=2)

    def __unicode__(self):
        return "%s" % self.name
