# Generated by Django 5.1.6 on 2025-02-11 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rename_professormodule_professor_to_module'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModuleInstance',
            new_name='Module_Instance',
        ),
        migrations.RenameModel(
            old_name='Professor_to_Module',
            new_name='Professor_Module',
        ),
    ]
