from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductMovement, Product, Location
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=ProductMovement)
def create_profile(sender, instance,created, **kwargs):
   if created:
      print('A new user was created:')