# Generated by Django 2.2.24 on 2021-08-15 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0143_change_field_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'permissions': (('see_private_problem', 'See hidden problems'), ('edit_own_problem', 'Edit own problems'), ('create_organization_problem', 'Create organization problem'), ('edit_all_problem', 'Edit all problems'), ('edit_public_problem', 'Edit all public problems'), ('suggest_new_problem', 'Suggest new problem'), ('problem_full_markup', 'Edit problems with full markup'), ('clone_problem', 'Clone problem'), ('change_public_visibility', 'Change is_public field'), ('change_manually_managed', 'Change is_manually_managed field'), ('see_organization_problem', 'See organization-private problems')), 'verbose_name': 'problem', 'verbose_name_plural': 'problems'},
        ),
    ]
