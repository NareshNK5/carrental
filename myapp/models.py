from django.db import models

# Create your models here.
class adminlog(models.Model):
	Username=models.CharField(max_length=30)
	Password=models.CharField(max_length=15)
	class Meta:
		db_table="adminlog"


class addk(models.Model):
	Photo=models.FileField(max_length=300, upload_to='',blank=True,null=True)
	Details=models.CharField(max_length=20)
	Model=models.CharField(max_length=20)
	Color=models.CharField(max_length=20)
	CarNumber=models.CharField(max_length=20)
	Seats=models.IntegerField()
	DriverCharge=models.CharField(max_length=20)
	OnroadCharge=models.CharField(max_length=20)
	ACCharge=models.CharField(max_length=20)
	offer=models.CharField(max_length=100)
	
	class Meta:
		db_table="addcars"

class bkdetail(models.Model):
	Firstname=models.CharField(max_length=20)
	Lastname=models.CharField(max_length=20)
	Email=models.CharField(max_length=20)
	Mobnum=models.CharField(max_length=20)
	Pickuploc=models.CharField(max_length=20)
	Droploc=models.CharField(max_length=20)
	Pickdate=models.CharField(max_length=20)
	Picktime=models.CharField(max_length=20)
	NumofPersons=models.CharField(max_length=20)
	Ac=models.CharField(max_length=20)
	Request=models.CharField(max_length=300)
	Payment=models.CharField(max_length=50)
	carno=models.CharField(max_length=50)
	offer=models.CharField(max_length=200)
	class Meta:
		db_table="customers"

class feed(models.Model):
	Name=models.CharField(max_length=40)
	mobile=models.CharField(max_length=100)
	Cusfeedback=models.CharField(max_length=200)
	Answer=models.CharField(max_length=100)
	
	class Meta:
		db_table="feedback"

class customerreg(models.Model):
	name=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	address=models.CharField(max_length=200)

	class Meta:
		db_table="tblcustreg"

class triparea(models.Model):
	area=models.CharField(max_length=200)

	class Meta:
		db_table="tbltriparea"

class offer(models.Model):
	carid=models.CharField(max_length=200)
	carnumber=models.CharField(max_length=200)
	offer=models.CharField(max_length=200)

	class Meta:
		db_table="tblcaroffer"