# Generated by Django 5.0 on 2024-01-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkurs', '0006_remove_student_is_dead_student_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]
