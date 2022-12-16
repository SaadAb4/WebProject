# Generated by Django 4.1.4 on 2022-12-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework3', '0007_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=50)),
                ('answer', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
    ]
