# Generated by Django 5.1.6 on 2025-02-21 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_rename_moduleinstance_module_instance_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Module_Instance',
            new_name='ModuleInstance',
        ),
        migrations.RenameModel(
            old_name='Professor_Module',
            new_name='ProfessorModule',
        ),
    ]
