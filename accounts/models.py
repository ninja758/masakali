from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self, mobile,  password=None, isActive=True, isStaff=False, isAdmin=False, chips=0):
        if not mobile:
            raise ValueError("MobileNumber is Required")
        if not password:
            raise ValueError("Password is Required")
        
        user_obj = self.model(
            mobile = mobile,
        )
        user_obj.mobileConfirm = False
        user_obj.set_password(password)
        user_obj.staff = isStaff
        user_obj.active = isActive
        user_obj.admin = isAdmin
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, mobile, password=None, chips=0):
        user_obj = self.create_user(
            mobile,
            password=password,
            isStaff=True,
            isAdmin=True,
            chips = chips
        )
        return user_obj
    def create_staffuser(self, mobile, email, name, password=None):
        user_obj = self.create_user(
            mobile,
            password=password,
            isStaff=True
        )
        return user_obj
    

class User(AbstractBaseUser):
    mobile = models.CharField(max_length=10, unique=True)
    chips = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    mobileConfirm = models.BooleanField(default=False)
    
    USERNAME_FIELD ="mobile"
    objects = UserManager()
    def __str__(self):
        return self.mobile

    def __chips__(self):
        return self.chips
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property 
    def is_active(self):
        return self.active

    @property
    def is_verified(self):
        return self.mobileConfirm

class otpModel(models.Model):
    id = models.AutoField(primary_key=True)
    phonenumber = models.BigIntegerField(unique=True, )
    otp = models.IntegerField()
    current_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    attempt = models.IntegerField(default=1)
