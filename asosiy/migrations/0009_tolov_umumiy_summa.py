# Generated by Django 4.1.9 on 2023-09-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0008_remove_yechib_olish_tolov_fk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tolov',
            name='umumiy_summa',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
