from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Customer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Saves the related Customer profile instance whenever the User instance is saved.
    """
    instance.customer.save()


@receiver(post_delete, sender=Customer)
def delete_user_profile(sender, instance, **kwargs):
    """
    Delete the associated User instance when a Customer profile is deleted.
    """
    if instance.user:
        instance.user.delete()
