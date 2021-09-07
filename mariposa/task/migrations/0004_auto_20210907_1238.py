# Generated by Django 3.2.6 on 2021-09-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210904_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TD', 'Todo'), ('DG', 'Doing'), ('DN', 'Done')], default='TD', max_length=2),
        ),
    ]
