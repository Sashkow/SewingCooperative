from django.shortcuts import render
from django.http import HttpResponse
import random

def generate_2_dice_random_value():
	sides = 6
	return random.randrange(1,sides+1) + \
		   random.randrange(1,sides+1)


def rolldice(request):
	# dice_value = generate_2_dice_random_value()
	return render(request, "rolldice/index.html",{'dice':'none'})

def rolldice_ajax(reqest):
	dice_value = generate_2_dice_random_value()
	location_url = {
		'squat': 'http://cs605820.vk.me/v605820495/46ff/FueILKAE2Go.jpg', 
		'friendorg': 'http://gloss.ua/file/12/08/03/wdtaw.JPG', 
		'rent': 'http://cv.mvs.gov.ua/mvs/img/publishing/?id=957118'
	}
	location = ''
	if dice_value <= 4:
		location = 'squat'
	elif dice_value > 4 and dice_value <= 8:
		location = 'friendorg'
	else:
		location = 'rent'
	resp = str(dice_value)+"|"+str(location_url[location])
	print resp
	return HttpResponse(resp)
