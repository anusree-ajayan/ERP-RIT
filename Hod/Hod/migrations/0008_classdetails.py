# Generated by Django 3.2 on 2021-06-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hod', '0007_alter_department_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDetails',
            fields=[
                ('classid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('courseid', models.CharField(max_length=50)),
                ('semid', models.IntegerField()),
                ('branch_or_specialisation', models.CharField(max_length=100)),
                ('deptname', models.CharField(max_length=100)),
                ('active', models.TextField()),
            ],
            options={
                'db_table': 'class_details',
                'managed': False,
            },
        ),
    ]
