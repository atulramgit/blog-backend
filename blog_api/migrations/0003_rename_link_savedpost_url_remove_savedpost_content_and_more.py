# Generated by Django 5.1.3 on 2024-12-11 17:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_alter_comment_user_name_savedpost'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedpost',
            old_name='link',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='savedpost',
            name='content',
        ),
        migrations.RemoveField(
            model_name='savedpost',
            name='saved_at',
        ),
        migrations.AlterField(
            model_name='savedpost',
            name='post_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='savedpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
