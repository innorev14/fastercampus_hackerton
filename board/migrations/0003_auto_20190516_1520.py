# Generated by Django 2.2.1 on 2019-05-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
    ]