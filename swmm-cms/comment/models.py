from django.db import models
from attribute.models import *

class Thread (models.Model):

    name = models.CharField (max_length=256)

    number_of_comments = property (
        lambda self: Comment.objects.filter (thread=self).count ()
    )

    def __unicode__(self):
        return "%s" % self.name
    
class  Comment (models.Model):

    thread = models.ForeignKey (Thread)
    text = models.TextField (max_length=4096)

    timestamp = models.DateTimeField (auto_now_add=True)
    username = models.CharField (max_length=256)
    email = models.EmailField (max_length=256)

    attributes = models.ManyToManyField (Attribute)

    def __unicode__(self):
        return "%s @ %s" % (self.thread, self.timestamp)
