from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField

class Student(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")  # ,второй аргумент используется Админ панеле
    birthday = models.DateField(blank=True, null=True,verbose_name="День рождения")
    content = models.TextField(blank=True,verbose_name="Контент")  # ,второй аргумент используется Админ панеле
    photo = ResizedImageField(size=[1000, 1000], upload_to="photos/appkurs",
                              blank=True, null=True,verbose_name="Фото")
    # ResizedImageField Изменение до сохранение
    is_live = models.BooleanField(default=True,verbose_name="Жив")
    grp = models.ForeignKey('Group',on_delete=models.PROTECT,null=True,verbose_name="Группа")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии' # Множественное число
        ordering = ['grp']

class Group(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name="Группа")  # ,второй аргумент используется Админ панеле

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('group', kwargs={'grp_id': self.pk})

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'   # Множественное число
        ordering = ['name']
#-----------------------------------------------------------------------
