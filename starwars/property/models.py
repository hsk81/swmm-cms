from django.db import models

class PropertyType (models.Model):

    name = models.CharField (max_length=32)
    regex = models.CharField (max_length=32)

    def __unicode__(self):
        return "%s" % self.name

class Property (models.Model):

    class Meta:

        verbose_name_plural = 'properties'

    name = models.CharField (max_length=32)
    type = models.ForeignKey (PropertyType)

    def __unicode__(self):
        return "%s" % self.name

    def values (name):
        
        return PropertyValue.objects.filter (
            property = Property.objects.get (name = name)
        )

    values = staticmethod (values)

    def value (name): ## first

        return Property.values (name)[0]

    value = staticmethod (value)

    def values_ (self):
        return Property.values (self.name)

    def value_ (self):
        return Property.value (self.name)

class PropertyValue (models.Model):

    property = models.ForeignKey (Property)
    data = models.CharField (max_length=256)

    def __unicode__(self):
        return "%s" % self.data
