# Generated by Django 5.0 on 2024-09-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_breakfast'),
    ]

    operations = [
        migrations.CreateModel(
            name='lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('food_name', models.CharField(max_length=255)),
                ('food_ingredients', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
