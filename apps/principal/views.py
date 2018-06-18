# -*- coding: utf-8 -*-
""" #Autores
	#Miguel Angel Medina Coaquira
	#Heber Uraccahua Barrios
"""

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from models import Follower

from django.http import JsonResponse

# Main page
def principal(request):

	seguidores = Follower.objects.all()

	return render(request, 'index.html', {'seguidores':seguidores})
	
# Save a follower
def guardar(request):
	#return HttpResponse('hola home')
	name = request.POST.get('name')
	mail = request.POST.get('mail')
	seguidor = Follower()

	seguidor.fol_name = name
	seguidor.fol_mail = mail
	seguidor.save()
	
	seguidores = Follower.objects.all()
	
	return render(request, 'index.html', {'seguidores':seguidores})
	

import json
import os
# Save a follower
def generar(request):
	#return HttpResponse('hola home')
	fact = {}
	fact['tipOperacion'] = ''
	fact['fecEmision'] = ''
	fact['codLocalEmisor'] = ''
	fact['tipDocUsuario'] = ''
	fact['numDocUsuario'] = ''
	fact['rznSocialUsuario'] = ''
	fact['tipMoneda'] = ''
	fact['sumDsctoGlobal'] = ''
	fact['sumOtrosCargos'] = ''
	fact['mtoDescuentos'] = ''
	fact['mtoOperGravadas'] = ''
	fact['mtoOperInafectas'] = ''
	fact['mtoOperExoneradas'] = ''
	fact['mtoIGV'] = ''
	fact['mtoISC'] = ''
	fact['mtoOtrosTributos'] = ''
	fact['mtoImpVenta'] = ''
	
	items = {}
	items['codUnidadMedida'] = ''
	items['ctdUnidadItem'] = ''
	items['codProducto'] = ''
	items['codProductoSUNAT'] = ''
	items['desItem'] = ''
	items['mtoValorUnitario'] = ''
	items['mtoDsctoItem'] = ''
	items['mtoIgvItem'] = ''
	items['tipAfeIGV'] = ''
	items['mtoIscItem'] = ''
	items['tipSisISC'] = ''
	items['mtoPrecioVentaItem'] = ''
	items['mtoValorVentaItem'] = ''
	
	fact['lstItems'] = items
	
	dir = r'E:\unsa\IIS\sunat_archivos\sfs\DATA'  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
	file_name = "data.cab"

	with open(os.path.join(dir, file_name), 'w') as file:
		json.dump(fact, file)
	
	print "hola, mundo!"
	
	return JsonResponse(fact)