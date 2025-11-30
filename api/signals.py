from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        print(f"Yangi product yaratildi: {instance.title}")
    else:
        print(f"Product yangilandi: {instance.title}")
