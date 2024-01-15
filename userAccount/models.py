from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    actualActivity = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    adress = models.TextField(max_length=250)
    cv = models.URLField(null=True)
    genPres = models.TextField(null=True, max_length=1000)
    threeGoodPoints = models.TextField(null=True)
    #availability = models.ArrayField(models.CharField(max_length=100)) #A modifier pour choix multiple
    threeExperiences = models.TextField(null=True)
    phone_number = models.CharField(max_length=20)

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