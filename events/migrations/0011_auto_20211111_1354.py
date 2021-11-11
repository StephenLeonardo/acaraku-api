# Generated by Django 3.1.3 on 2021-11-11 06:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20211109_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/11-2021/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/11-2021/'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False),
        ),
    ]
