from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()


# Create your models here.
class Scholarship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=30, null=True, blank=True)
    contact1 = models.CharField(max_length=30, null=True, blank=True)
    contact2 = models.CharField(max_length=30, null=True, blank=True)
    birth = models.FileField(upload_to='%s/birth/'.format(user), null=True, blank=True)
    naid = models.FileField(upload_to='%s/naid/'.format(user), null=True, blank=True)
    letter = models.FileField(upload_to='%s/letter/'.format(user), null=True, blank=True)
    school = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    level = models.CharField(max_length=500, null=True, blank=True)
    year = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=500, null=True, blank=True)
    approved = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.names)


# sponsor model
class Sponsor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sponsor = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)
