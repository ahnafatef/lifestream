from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Donor(models.Model):
	A_POS  = 'A+'
	A_NEG  = 'A-'
	B_POS  = 'B+'
	B_NEG  = 'B-'
	AB_POS = 'AB+'
	AB_NEG = 'AB-'
	O_POS  = 'O+'
	O_NEG  = 'O-'
	BLOOD_GROUP_CHOICES = [
		(A_POS, 'A+ (positive)'),
		(A_NEG, 'A- (negative)'),
		(B_POS, 'B+ (positive)'),
		(B_NEG, 'B- (negative)'),
		(AB_POS, 'AB+ (positive)'),
		(AB_POS, 'AB- (negative)'),
		(O_POS, 'O+ (positive)'),
		(O_POS, 'O- (negative)'),
	]


	# name
	name = models.CharField(
		max_length=30,
		default=''
		)

	# blood group choices
	blood_group = models.CharField(
		max_length=3,
		choices = BLOOD_GROUP_CHOICES,
		default=O_POS,
	)

	# gender
	gender = models.CharField(
		max_length=1,
		choices = [('m', 'Male'), ('f', 'Female')]
	)

	# age
	age = models.IntegerField(validators=[MinValueValidator(17), MaxValueValidator(70)])

	# location
	location = models.CharField(max_length=100, default='')

	# phone
	phone_regex = RegexValidator(regex=r'^[0]{1}[\d]{10}',
		message="Phone number must be of the form: 01XXXXXXXXX")
	phone_number = models.CharField(validators=[phone_regex], max_length=11, default='')