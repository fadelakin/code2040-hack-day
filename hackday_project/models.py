from django.db import models


class Grocery(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        managed = True
        db_table = 'groceries'

    def __unicode__(self):
        return self.name


class Family(models.Model):
    family_name = models.CharField(max_length=255)
    family_photo = models.FileField(null=True, blank=True)
    description = models.CharField(max_length=1024)
    groceries = models.ManyToManyField(Grocery, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'family'

    def __unicode__(self):
        return self.family_name


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    families_donated = models.ManyToManyField(Family)

    class Meta:
        managed = True
        db_table = 'users'

    def __unicode__(self):
        return self.email
