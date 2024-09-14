from django.db import models

class Films_post(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    text1 = models.TextField('Описание фильма')
    text2 = models.TextField('Отзыв о фильме')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
