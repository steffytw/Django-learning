# Generated by Django 3.0.6 on 2020-06-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name_plural': 'Registration Details'},
        ),
    ]