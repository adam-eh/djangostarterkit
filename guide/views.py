from django.template.response import SimpleTemplateResponse

def index(request):
	return TemplateResponse(request, 'index.html')

def newb(request):
	return TemplateResponse(request, 'newb.html')

def py_newb(request):
	return TemplateResponse(request, 'py_newb.html')

def django_newb(request):
	return TemplateResponse(request, 'django_newb.html')
