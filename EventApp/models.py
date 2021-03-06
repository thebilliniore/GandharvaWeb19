from django.db import models

# Create your models here.


class EventMaster(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=100)
    num_of_winners = models.IntegerField()
    team_size = models.IntegerField()
    entry_fee = models.IntegerField()
    objective = models.CharField(max_length=300)
    round1 = models.CharField(max_length=300)
    round2 = models.CharField(max_length=300)
    rules = models.CharField(max_length=30)

    def __str__(self):
        return self.event_name

# model for Department


class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    img = models.CharField(max_length=200)
    link_to = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EventDepartment(models.Model):
    event = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class SponsorMaster(models.Model):
    sponsor_name = models.CharField(max_length=30)
    sponsor_logo = models.CharField(max_length=200)
    sponsor_info = models.CharField(max_length=200, default='No Info. Available')

    def __str__(self):
        return self.sponsor_name


class Carousel(models.Model):
    src = models.CharField(max_length=200)

