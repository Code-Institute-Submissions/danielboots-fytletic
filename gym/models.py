from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):

    # Meta Class overwrites Django 'S' to our stated plural metaclass.
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gym(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    # Address Fields.

    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)

    # Contact
    email = models.CharField(
        max_length=50, null=False, blank=False, default="DEFAULT VALUE"
    )
    whatsapp = models.CharField(
        max_length=50, null=False, blank=False, default="DEFAULT VALUE"
    )

    # Media
    gym_photo_main = models.ImageField(
        upload_to="media/%Y/%m/%d", null=True, blank=True
    )
    video = models.URLField(null=True, blank=True)
    photo_1 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True)

    # Social
    facebook = models.URLField(max_length=1024, null=True, blank=True)
    instagram = models.URLField(max_length=1024, null=True, blank=True)
    twitter = models.URLField(max_length=1024, null=True, blank=True)
    web = models.URLField(max_length=1024, null=True, blank=True)

    # Misc
    is_verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
