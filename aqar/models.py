from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your model here.
class Property(models.Model):
    property_name = models.CharField(
        max_length=255,
        help_text="Name or title of the property."
    )

    property_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Price of the property (e.g., 1500000.00)."
    )

    property_age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
        default=0,
        help_text="Age of the property in years (0–100)."
    )

    property_street_width = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Width of the street in meters."
    )

    property_rooms = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of rooms in the property."
    )

    property_area = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Area of the property in square meters."
    )

    property_kitchen = models.BooleanField(default=False)
    property_garage = models.BooleanField(default=False)
    availability_of_water = models.BooleanField(default=False)
    availability_of_sanitation = models.BooleanField(default=False)
    property_swimming_pool = models.BooleanField(default=False)
    
    advertising_license_number = models.BigIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Government-issued advertising license number."
    )

    property_Interface = models.BooleanField(default=False)
    
    property_Lounge = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of lounges in the property."
    )

    property_furnished = models.BooleanField(default=False)
    property_annex = models.BooleanField(default=False)
    property_air_conditioner = models.BooleanField(default=False)
    availability_of_electricity = models.BooleanField(default=False)
    property_yard = models.BooleanField(default=False)

    Number_of_visits = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Total number of times this listing has been visited."
    )

    Val_license_number = models.BigIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Valuation license number."
    )

    property_location = models.URLField(
        max_length=500,
        help_text="Google Maps or location URL for the property."
    )

    property_images = models.ImageField(
        upload_to='property_images/',
        help_text="Upload an image of the property."
    )

    property_video = models.FileField(
        upload_to='property_videos/',
        null=True,
        blank=True,
        help_text="Optional video tour of the property."
    )

    property_ads_textarea = models.TextField(
        help_text="Detailed description of the property advertisement."
    )

    def __str__(self):
        return self.property_name


