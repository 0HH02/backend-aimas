# Generated by Django 4.2.6 on 2023-10-21 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.BooleanField(default=False, help_text='Tiene sitio web'),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('OP1', '-IMPLEMENTADO-'), ('OP2', '-PROXIMO A IMPLEMENTARSE-'), ('OP3', '-PROPUESTA-')], default='OP2', max_length=3),
        ),
    ]