# Generated by Django 3.2.8 on 2021-12-18 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_videourl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='concluded',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='concluded',
        ),
        migrations.RemoveField(
            model_name='module',
            name='concluded',
        ),
        migrations.AddField(
            model_name='lesson',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='lesson_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='module',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='module_author', to='courses.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DoneLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_lesson', to='courses.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
