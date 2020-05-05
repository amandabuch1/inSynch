# Generated by Django 3.0.4 on 2020-05-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('A', 'Angry'), ('B', 'Melancholy'), ('C', 'Cheerful'), ('D', 'Calm'), ('E', 'Romantic'), ('F', 'Mysterious')], default='A', max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('band', models.CharField(max_length=100)),
            ],
        ),
    ]