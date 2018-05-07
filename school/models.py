from django.db import models

# Create your models here.
class Schools(models.Model):
    reg_number=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=20)
    teacher_no=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='schools'
        verbose_name_plural='schools'

#This is the abtract class;
class CommonInfo(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    middle_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=False)

    class Meta:
        abstract=True

class Heads(CommonInfo):
    phone=models.CharField(max_length=13)
    tsc_no=models.IntegerField()
    school_reg=models.ForeignKey(Schools,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+" "+self.last_name

    class Meta:
        db_table='heads'
        verbose_name_plural='heads'


