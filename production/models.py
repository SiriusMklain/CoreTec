from django.db import models


class Brand(models.Model):
    """Бренд"""
    name = models.CharField(verbose_name="Бренд", max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = "Бренд>"
        verbose_name_plural = "Бренды"
        db_table = 'brand'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """Категории продукции"""
    name = models.CharField(verbose_name="Имя категории", max_length=100)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория продукции"
        verbose_name_plural = "Категории продукции"
        db_table = 'category_product'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Продукция"""
    category = models.ForeignKey(ProductCategory, verbose_name="Категория", on_delete=models.CASCADE,
                                 db_constraint="name")
    name = models.CharField(verbose_name="Имя комплектуещей", max_length=250)
    quantity = models.IntegerField(verbose_name="Клличество")

    class Meta:
        ordering = ('name',)
        verbose_name = "Комплектующия"
        verbose_name_plural = "Комплектующии"
        db_table = 'product'

    def __str__(self):
        return self.name
