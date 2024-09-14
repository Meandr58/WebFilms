# Generated by Django 5.1.1 on 2024-09-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название фильма')),
                ('text1', models.TextField(verbose_name='Описание фильма')),
                ('text2', models.TextField(verbose_name='Отзыв о фильме')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
