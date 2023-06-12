from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'landing.html')

class UsuariosView(TemplateView):
    template_name = "usuarios.html"
    
    def get(self, request):
        usuarios = User.objects.all()
        context = {"usuarios": usuarios}
        return render(request, "usuarios.html", context)
