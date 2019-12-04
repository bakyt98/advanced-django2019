# Generated by Django 2.2.5 on 2019-12-04 11:32

from django.db import migrations, models
import utils.file_utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191204_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdocument',
            name='document',
            field=models.FileField(upload_to='files/', validators=[utils.file_utils.validate_image_size]),
        ),
    ]