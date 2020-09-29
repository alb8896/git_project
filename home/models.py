from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    article = models.CharField(max_length=20, verbose_name='артикул', unique=True, null=True)
    description = models.TextField(verbose_name='описание', null=True)
    price = models.FloatField(verbose_name='цена')
    img = models.ImageField(default='default.jpg', upload_to='media',
                            verbose_name='фото')  # height_field=100, width_field=100,

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Cart(models.Model):
    user_cart = models.ForeignKey(CustomUser, verbose_name='владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductAdd, blank=True)
    price_summ = models.FloatField(verbose_name='сумма заказа')

    def __str__(self):
        return self.products


class ProductAdd(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='пользователь', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество')
    price_summ = models.FloatField(verbose_name='сумма заказа')

    def __str__(self):
        return self.product



