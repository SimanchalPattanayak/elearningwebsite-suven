# Generated by Django 3.1.1 on 2020-09-29 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0011_auto_20200929_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='curriculum.comment'),
        ),
    ]
