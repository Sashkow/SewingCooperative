from django.shortcuts import render
import random

def generate_2_dice_random_value():
	sides = 6
	return random.randrange(1,sides+1) + \
		   random.randrange(1,sides+1)


def rolldice(request):
	dice_value = generate_2_dice_random_value()
	return render(request, "rolldice/index.html",{'dice':dice_value})
