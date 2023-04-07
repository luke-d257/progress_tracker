# Generated by Django 4.1.3 on 2023-04-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('percOfComp', models.IntegerField()),
                ('idealPerc', models.IntegerField()),
            ],
        ),
    ]