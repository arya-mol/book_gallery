from django.db import models

# Create your models here.

class Districts(models.Model):
    dist_name=models.CharField(max_length=120,unique=True)
    population=models.PositiveIntegerField()
    firstdosevaccinationrate=models.PositiveIntegerField()
    seconddosevaccinationrate=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.dist_name




# ORM queries for listing all district
# district=Districts.objects.all()
# district

# print all details of idukki
# district=Districts.objects.get(id=1)
# district
# print(district.dist_name,district.population)

# print all details whoes population<500000
# districts=Districts.objects.filter(population__lt=500000)
# districts

# print all details whoes population>500000
# districts=Districts.objects.filter(population__gt=500000)
# districts

# print all details whoes population>=600000
# districts=Districts.objects.filter(population__gte=600000)
# districts

# print all details whoes population<=600000
# districts=Districts.objects.filter(population__lte=600000)
# districts

# print all details whoes population range 400000 to 800000
# districts=Districts.objects.filter(population__gte=400000,population__lte=800000)
# districts

# print all details whoes active_status="False"
# districts=Districts.objects.filter(active_status=False)
# districts


# print number of inactive district names
# districts=Districts.objects.filter(active_status=False).count()
# districts

# print details whoes population=200000
# district=Districts.objects.filter(population=200000)
# district

# print maximum population
# population_max=Districts.objects.all().aggregate(Max("population"))
# population_max

# print minimum population
# population_min=Districts.objects.all().aggregate(Min("population"))
# population_min

# update first dose vaccination rate in id=2
# district=Districts.objects.get(id=2)
# district
# district.firstdosevaccinationrate=60
# district.save()





