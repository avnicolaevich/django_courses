# Generated by Django 4.1.7 on 2023-03-21 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_8', '0002_rename_gender_gamemodel_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='lesson_8.gamemodel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_8.gamermodel')),
            ],
        ),
    ]
