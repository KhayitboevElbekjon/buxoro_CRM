# Generated by Django 4.1.9 on 2023-07-17 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinov',
            name='sorov_fk',
        ),
        migrations.AddField(
            model_name='sinov',
            name='kutish_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.kutish'),
        ),
    ]
