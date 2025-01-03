from django.db import models
# allows generic releationships
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

# custom managers for tags


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return TaggedItem.objects\
            .select_related('tag')\
            .filter(content_type=content_type, object_id=obj_id)


class Tag(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    object = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # To define a Generic relationship, we need three fields; content_type, object_id and content_object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
