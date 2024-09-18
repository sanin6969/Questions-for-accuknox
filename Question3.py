from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

@receiver(post_save, sender=Product)
def product_signal_handler(sender, instance, created, **kwargs):
    print(f'Signal received for {instance.name} with price {instance.price}')
    if instance.price < 0:
        raise ValidationError('Price cannot be negative.')

if __name__ == '__main__':
    try:
        with transaction.atomic():
            print('Creating product...')
            product = Product(name='Test Product', price=20.00)
            product.save()
            print('Product created successfully.')
            print('Creating product with negative price...')
            invalid_product = Product(name='Invalid Product', price=-10.00)
            invalid_product.save()
            print('This line will not be reached due to the error.')

    except ValidationError as e:
        print(f'Error occurred: {e}')
    print('Number of products in the database:', Product.objects.count())
