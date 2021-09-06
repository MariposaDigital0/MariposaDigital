# Generated by Django 3.2.6 on 2021-09-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('TD', 'Todo'), ('DG', 'Doing'), ('DN', 'Done')], default='TD', max_length=2),
        ),
    ]
