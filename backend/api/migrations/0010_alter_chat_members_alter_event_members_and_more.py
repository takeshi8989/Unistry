# Generated by Django 4.1.5 on 2023-01-14 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to='api.profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='event_members', to='api.profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='static/user_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.school'),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to='api.profile'),
        ),
    ]
