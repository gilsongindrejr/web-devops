from django.http import HttpResponse

def index(request):
    html = "<html><body><h2>Aplicação desenvolvida para a matéria de Devops</h2></html></body>"
    return HttpResponse(html)

