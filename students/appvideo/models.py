from django.core.validators import FileExtensionValidator
from django.db import models
from django_resized import ResizedImageField

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # ResizedImageField Изменение до сохранение
    image = ResizedImageField(size=[200, 200], upload_to='photos/appvideo/',
                              blank=True, null=True,verbose_name="Фото")
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
