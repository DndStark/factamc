from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def principal(request):
	#return JsonResponse({'foo':'bar'})
	#return render(request, 'templates/test.html', {})
	return HttpResponse('hola test')
		

