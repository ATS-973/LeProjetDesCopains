from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
import django.utils.timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    actual_activity = models.CharField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    adress = models.TextField(max_length=250, blank=True, null=True)
    cv = models.URLField(blank=True, null=True)
    general_presentation = models.TextField(blank=True, max_length=1000, null=True)
    three_good_points = models.TextField(blank=True, null=True)
    #availability = models.ArrayField(models.CharField(max_length=100)) #A modifier pour choix multiple
    three_experiences = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=django.utils.timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name=('groups'),
        help_text=('The groups this user belongs to.'),
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name=('user permissions'),
        help_text=('Specific permissions for this user.'),
    )