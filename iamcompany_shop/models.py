from django.db import models
from django.shortcuts import reverse

# Класс категорий
class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Категория")
    slug = models.SlugField(null = False, unique = True, verbose_name = "URL")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
   
    
# Класс продукта
class Product(models.Model):
    # Информация
    title = models.CharField(max_length = 50, verbose_name = "Название")
    product_photo = models.ImageField(upload_to = 'static/images', verbose_name = "Фото") 
    cost = models.IntegerField(null = False, verbose_name = "Цена")
    category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE, verbose_name = "Категория")
    size = models.IntegerField(null = False, verbose_name = "Длинна мм")
    weight = models.CharField(max_length = 10, null = False, verbose_name = "Вес гр")
    slug = models.SlugField(null = False, unique = True, verbose_name = "URL")  

    def __str__(self):
        return self.title
        
    class Meta:
        db_table = "ProductModel"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"
