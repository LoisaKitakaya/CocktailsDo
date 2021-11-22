# Generated by Django 3.2.9 on 2021-11-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinksData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_posting', models.CharField(max_length=50)),
                ('drink_name', models.CharField(max_length=50)),
                ('drink_image', models.ImageField(upload_to='uploads/')),
                ('drink_ingredients', models.TextField()),
                ('drink_instructions', models.TextField()),
                ('drink_glass', models.CharField(choices=[('HG', 'Highball Glass'), ('SG', 'Shot Glass'), ('RG', 'Rock Glass'), ('CG', 'Coupe Glass'), ('MG', 'Martini Glass'), ('TG', 'Margarita Glass'), ('NG', 'Hurricane Glass')], max_length=50)),
                ('drink_category', models.CharField(choices=[('AN', 'Ancestral'), ('SO', 'Sours'), ('SF', 'Spirit Forward'), ('DT', 'Duos & Trios'), ('CC', 'Champagne Cocktails'), ('HCF', 'Highballs, collinses & Fizzes'), ('JS', 'Juleps & smashes'), ('HD', 'Hot drinks'), ('FN', 'Flips & Nogs'), ('PF', 'Pousse family')], max_length=50)),
            ],
        ),
    ]
