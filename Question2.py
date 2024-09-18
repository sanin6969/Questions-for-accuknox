from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()


@receiver(post_save, sender=Order)
def order_sgnal(sender, instance, created, **kwargs):
    if created:
        print(f'Order created: Product - {instance.product_name}, Quantity - {instance.quantity}')
    else:
        print(f'Order updated: Product - {instance.product_name}, Quantity - {instance.quantity}')


if __name__ == '__main__':
    order = Order(product_name='Laptop', quantity=2)
    order.save()
    order.quantity = 3
    order.save()
