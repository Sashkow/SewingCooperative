from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

import json
from django.shortcuts import *
from django.template import RequestContext
from rolldice.forms import AdvertForm

def advert(request):
    if request.method == "POST":
        form = AdvertForm(request.POST)

        
        if(form.is_valid()):
            print(request.POST['dice1'])
            dice1 = request.POST['dice1']
            dice2 = request.POST['dice1']

        return HttpResponse(json.dumps({'dice1': dice1, 'dice2': dice2}))

    return render(request, 'rolldice/index.html', {'form':AdvertForm()})