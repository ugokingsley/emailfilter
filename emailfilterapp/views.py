from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings as django_settings
from .forms import *
from django.contrib import messages
from contextlib import closing
from django.db import connection
from django.utils import timezone
import re



# Create your views here.
def index(request):
	text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"


	emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
	if request.method == 'GET':
		form = EmailFilterForm()

	if request.method == 'POST':
		form = EmailFilterForm(request.POST)
		if form.is_valid():
			
			message = form.cleaned_data['message']
			msg_id = message
			'''
			try:
				send_mail(name, msg_id, email, ['samuelngoke@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			'''
			messages.success(request, 'Successful, Thanks for your message')
			return redirect('/')

	else:
		form = EmailFilterForm()

	return render(request, 'index.html', {
        'form': form,
        "emails":emails,
    })