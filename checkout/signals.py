from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import CheckoutLine


@receiver(post_save, sender=CheckoutLine)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()


@receiver(post_delete, sender=CheckoutLine)
def delete_on_save(sender, instance, **kwargs):

    instance.order.update_total()
