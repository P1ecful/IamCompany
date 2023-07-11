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
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
   
    
# Класс продукта
class Product(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Название")
    product_photo = models.ImageField(upload_to = 'static/images/catalog_src', verbose_name = "Фото") 
    cost = models.IntegerField(null = False, verbose_name = "Цена")
    category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE, verbose_name = "Категория", related_name = 'categories')
    slug = models.SlugField(null = False, unique = True, verbose_name = "URL") 
    size = models.IntegerField(null = False, verbose_name = "Длина мм")
    weight = models.CharField(max_length = 10, null = False, verbose_name = "Вес гр") 

    def __str__(self):
        return self.title
        
    class Meta:
        db_table = "ProductModel"
        verbose_name = "Продукты"
        verbose_name_plural = "Продукт"

# Класс баннеров для главное страницы
class Banner(models.Model):
    title = models.CharField(max_length = 55, verbose_name = "Название")
    photo = models.ImageField(upload_to = 'static/images/banner_src', verbose_name = "Фото")
    isPublished = models.BooleanField(null = False, default = False, verbose_name = "Опубуликован")

    class Meta:
        db_table = "BannerModel"
        verbose_name = "Баннеры"
        verbose_name_plural = "Баннер"