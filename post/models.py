from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'

class Settings2(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'

class Settings3(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'

class Settings4(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'

class Settings5(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта' 

class Menu(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Меню'
        verbose_name_plural='Меню'

class About(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'



class Shop(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Магазин'
        verbose_name_plural='Магазин'

class Shop_Details(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Подробности магазина'
        verbose_name_plural='Подробности магазина'

class Cart(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Тележка'
        verbose_name_plural='Тележка'

class Wishlist(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Список желаний'
        verbose_name_plural='Список желаний'

class Checkout(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Оплата и доставка'
        verbose_name_plural='Оплата и доставка'

class Reservation(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Бронирование'
        verbose_name_plural='Бронирование'

class FAQ(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Часто задаваемые вопросы (FAQ)'
        verbose_name_plural='Часто задаваемые вопросы (FAQ)'

class Login(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Авторизация'
        verbose_name_plural='Авторизация'

class Signup(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Регистрация'
        verbose_name_plural='Регистрация'

class PNF(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='404'
        verbose_name_plural='404'

class Coming_Soon(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Вскоре'
        verbose_name_plural='Вскоре'

class Terms_Conditions(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Условия'
        verbose_name_plural='Условия'

class Blog_Details(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Подробности блога'
        verbose_name_plural='Подробности блога'

class Blogs(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Блог'
        verbose_name_plural='Блог'

class Contact(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Контакты'
        verbose_name_plural='Контакты'
        