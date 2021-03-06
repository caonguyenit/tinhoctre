# Generated by Django 2.2.26 on 2022-01-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0170_contest_data_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemdata',
            name='checker',
            field=models.CharField(choices=[('standard', 'Standard'), ('bridged', 'Custom checker'), ('floats', 'Floats'), ('floatsabs', 'Floats (absolute)'), ('floatsrel', 'Floats (relative)'), ('identical', 'Byte identical'), ('linecount', 'Line-by-line')], default='standard', max_length=10, verbose_name='checker'),
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='grader',
            field=models.CharField(choices=[('standard', 'Standard'), ('interactive', 'Interactive'), ('signature', 'Function Signature Grading (IOI-style)'), ('output_only', 'Output Only'), ('custom_judge', 'Custom Grader')], default='standard', max_length=30, verbose_name='Grader'),
        ),
    ]
