# Generated by Django 5.1.2 on 2024-10-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerData',
            fields=[
                ('PassengerId', models.IntegerField(primary_key=True, serialize=False)),
                ('Pclass', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Sex', models.CharField(max_length=10)),
                ('Age', models.FloatField()),
                ('Sibsp', models.IntegerField()),
                ('Ticket', models.CharField(max_length=255)),
                ('Fare', models.FloatField()),
                ('Cabin', models.CharField(blank=True, max_length=50, null=True)),
                ('Embarked', models.CharField(max_length=10)),
            ],
        ),
    ]
