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

    def update_rate (self, value):

        self.rate = '%s' % ((255.0/256.0)*float (self.rate) + (1.0/256.0)*value)

    def round (rate):

        if                    rate < 0.00: return 0.00
        elif rate >= 0.00 and rate < 0.25: return 0.00
        elif rate >= 0.25 and rate < 0.50: return 0.50
        elif rate >= 0.50 and rate < 0.75: return 0.50

        elif rate >= 0.75 and rate < 1.00: return 1.00
        elif rate >= 1.00 and rate < 1.25: return 1.00
        elif rate >= 1.25 and rate < 1.50: return 1.50
        elif rate >= 1.50 and rate < 1.75: return 1.50

        elif rate >= 1.75 and rate < 2.00: return 2.00
        elif rate >= 2.00 and rate < 2.25: return 2.00
        elif rate >= 2.25 and rate < 2.50: return 2.50
        elif rate >= 2.50 and rate < 2.75: return 2.50

        elif rate >= 2.75 and rate < 3.00: return 3.00
        elif rate >= 3.00:                 return 3.00

        else: return rate

    round = staticmethod (round)

    avg_rate = property (lambda obj: Image.round (float (obj.rate)))

    def __unicode__(self):

        return "%s" % self.name
