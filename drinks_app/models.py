from django.db import models
import datetime

# Create your models here.
class DrinksData(models.Model):
    # types of glasses and drink categories
    GLASSES = (
        ('HG', 'Highball Glass'),
        ('SG', 'Shot Glass'),
        ('RG', 'Rock Glass'),
        ('CG', 'Coupe Glass'),
        ('MG', 'Martini Glass'),
        ('TG', 'Margarita Glass'),
        ('NG', 'Hurricane Glass'),
    )

    CATEGORIES = (
        ('AN', 'Ancestral'),
        ('SO', 'Sours'),
        ('SF', 'Spirit Forward'),
        ('DT', 'Duos & Trios'),
        ('CC', 'Champagne Cocktails'),
        ('HCF', 'Highballs, collinses & Fizzes'),
        ('JS', 'Juleps & smashes'),
        ('HD', 'Hot drinks'),
        ('FN', 'Flips & Nogs'),
        ('PF', 'Pousse family'),
    )

    # models
    person_posting = models.CharField(max_length=50)
    drink_name = models.CharField(max_length=50)
    drink_image = models.ImageField(upload_to='uploads/')
    drink_ingredients = models.TextField()
    drink_instructions = models.TextField()
    drink_glass = models.CharField(max_length=50, choices=GLASSES)
    drink_category = models.CharField(max_length=50, choices=CATEGORIES)
    date_posted = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.drink_name