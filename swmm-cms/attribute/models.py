from django.db import models

class AttributeKey (models.Model):

    content = models.CharField (max_length=32)

    def __unicode__(self):
        return "%s" % self.content

class AttributeValue (models.Model):

    content = models.TextField ()

    def __unicode__(self):
        return "%s" % self.content

class Attribute (models.Model):

    key = models.ForeignKey (AttributeKey)
    value = models.ForeignKey (AttributeValue)

    def __unicode__(self):
        return "%s: %s" % (self.key, self.value)
