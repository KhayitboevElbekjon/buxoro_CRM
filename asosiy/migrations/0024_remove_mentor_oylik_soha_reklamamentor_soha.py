# Generated by Django 4.1.9 on 2023-10-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0023_info_mentor_oylik_soha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor_oylik',
            name='soha',
        ),
        migrations.AddField(
            model_name='reklamamentor',
            name='soha',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
