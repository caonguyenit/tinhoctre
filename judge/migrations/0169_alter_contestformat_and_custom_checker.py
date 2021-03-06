# Generated by Django 2.2.24 on 2022-01-21 04:15

import django.core.validators
from django.db import migrations, models

import judge.models.problem_data
import judge.utils.problem_data


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0168_alter_allow_tagging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='format_name',
            field=models.CharField(choices=[('atcoder', 'AtCoder'), ('default', 'Default'), ('ecoo', 'ECOO'), ('icpc', 'ICPC'), ('ioi', 'IOI (pre-2016)'), ('ioi16', 'IOI'), ('vnoj', 'VNOJ')], default='default', help_text='The contest format module to use.', max_length=32, verbose_name='contest format'),
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='custom_checker',
            field=models.FileField(blank=True, null=True, storage=judge.utils.problem_data.ProblemDataStorage(), upload_to=judge.models.problem_data.problem_directory_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['cpp', 'py', 'pas'])], verbose_name='custom checker file'),
        ),
    ]
