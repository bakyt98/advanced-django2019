# Generated by Django 2.2.5 on 2019-12-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191112_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block_type',
            field=models.IntegerField(choices=[(1, 'TO DO'), (2, 'In progress'), (3, 'Done'), (99, 'New')], default=99),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('SOFTWARE', 'SOFTWARE'), ('WEB', 'WEB'), ('APP', 'APP')], default='SOFTWARE', max_length=100),
        ),
    ]
