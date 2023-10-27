# Generated by Django 4.2.6 on 2023-10-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='Blogs'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('-IMPLEMENTADO-', '-IMPLEMENTADO-'), ('-PROXIMO A IMPLEMENTARSE-', '-PROXIMO A IMPLEMENTARSE-'), ('-PROPUESTA-', '-PROPUESTA-')], default='-IMPLEMENTADO-', max_length=200),
        ),
    ]