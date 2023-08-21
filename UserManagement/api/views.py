from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from UserManagement.models import UserProfile


@login_required
def create_profile(request):
    user = request.user
    if request.method == 'POST':
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        UserProfile.objects.create(user=user, dob=dob, gender=gender, username=username)
        return HttpResponse('Good')
    return render(request, 'create_profile.html')
