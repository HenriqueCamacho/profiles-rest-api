from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):#None password won't work, need to be a hash, until set, we won't be able to authenticate the user
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email adress")
        
        #Normalize second half of the email --> Always case Insensitive
        #Some e-mail providers such as gmail, hotmail make the first half case insensitive to but could be case sensitive depending on the provider
        email = self.normalize(email)

        #Create user model
        user = self.model(email = email, name = name)
        #Equivalent of user=UserProfile(email= email, name = name)

        #Converted into a hash, never store in plain text
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password): #We wan't all user to have a password
        """Create and save a new superuser with given details"""        
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)#Standart specify a database, best Practise is self._db for supporting multiple db's
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length=255)
    
    #Fields for the permission system, comes from PermissionsMixin
    is_active= models.BooleanField(default = True) #Determine if the user profile is active or not, set default for true
    is_staff = models.BooleanField(default = False) #Determine if the user is a staff user(should have acess to the Django admin)

    #Specify the model managment for our objects, Django needs to have a custom model manager for the user model so it knows how to create/control users using comand line tools
    objects = UserProfileManager()

    #Add couple more fields to the class
    # Work with Django Admin and Django authentication system
    USERNAME_FIELD = 'email'  #Instead of username, use email to authenticate. Username(email) is required by default
    REQUIRED_FIELDS= ['name']

    
    #Add functions to Django interacts with the User model

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    #Return string representation of model
    def __str__(self):
        #Recomend for Django models, return the field we want to represent our model
        """Return string representation of our user"""
        return self.email

