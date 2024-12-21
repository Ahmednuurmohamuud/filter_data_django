from django.db import models

class Programmer(models.Model):
    pgno = models.IntegerField()
    pgname = models.CharField(max_length=30)
    pgsal = models.FloatField()
    pgaddr = models.CharField(max_length=30)
    pgemail = models.EmailField(null=True, blank=True)  # Correct placement of pgemail

    def __str__(self):
        return self.pgname


class Student(models.Model):  # Renamed to follow proper naming conventions
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    ssal = models.FloatField()
    saddr = models.CharField(max_length=30)

    def __str__(self):
        return self.sname


class SoftwareDeveloper(models.Model):  # Fixed naming conventions
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
