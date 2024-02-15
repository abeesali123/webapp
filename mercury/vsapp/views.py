from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
	if request.method == 'POST':
			message = request.POST.get('message')
			name = request.POST.get('name')
			email = request.POST.get('email')
			phone = request.POST.get('phone')

			ctx = {
				'name': name,
				'email': email,
				'phone': phone,
				'message': message,
			}
			message = render_to_string('mail.html', ctx)
			send_mail('Contact Form',
					  message,
					  settings.EMAIL_HOST_USER,
					  ['mercuryinfotech.site@gmail.com'],
					  fail_silently=False, html_message=message)
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')