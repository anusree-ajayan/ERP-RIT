# Generated by Django 3.2 on 2021-06-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hod', '0008_classdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAdvisor',
            fields=[
                ('classid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('students_list', models.TextField()),
            ],
            options={
                'db_table': 'staff_advisor',
                'managed': False,
            },
        ),
    ]
