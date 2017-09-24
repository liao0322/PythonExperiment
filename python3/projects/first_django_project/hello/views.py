from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user_list = User.objects.all()
    return render(request, 'table.html', {'user_list': user_list})
