# Generated by Django 2.0.6 on 2018-06-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_person_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120)),
                ('address', models.TextField(blank=True)),
                ('person', models.ManyToManyField(blank=True, to='api.Person')),
            ],
        ),
    ]