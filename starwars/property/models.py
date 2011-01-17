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

    def datas (name):

        datas = PropertyData.objects.filter (
            property = Property.objects.get (name = name)
        )

        return datas

    datas = staticmethod (datas)

    def data (name): ## first-or-default

        data = Property.datas (name)

        if len (data) > 0: return data[0]
        else:              return None

    data = staticmethod (data)

    def texts (name):

        texts = PropertyText.objects.filter (
            property = Property.objects.get (name = name)
        )

        return texts

    texts = staticmethod (texts)

    def text (name): ## first-or-default

        texts = Property.texts (name)

        if len (texts) > 0: return texts[0]
        else:               return None

    text = staticmethod (text)

class PropertyData (models.Model):

    class Meta:

        verbose_name_plural = 'property data'

    property = models.ForeignKey (Property)
    data = models.CharField (max_length=256)

    def __unicode__(self):
        return "%s" % self.data

class PropertyText (models.Model):

    property = models.ForeignKey (Property)
    text = models.TextField ()

    def __unicode__(self):
        return "%s" % self.text
