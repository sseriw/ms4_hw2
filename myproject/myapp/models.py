from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    description = models.TextField()  # Описание поста
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Изображение (необязательное)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания (автоматически)

    def __str__(self):
        return self.title
