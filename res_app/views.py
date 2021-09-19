from django import forms
from django.shortcuts import redirect, render, HttpResponseRedirect

# Create your views here.
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


class HomeView(View):

    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'res_app/home.html',
                      {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            subject = 'Resume Uploaded'
            message = f'Hi {request.POST["name"]}, thank you for registering Resume.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST["email"]]
            send_mail(subject, message, email_from, recipient_list)
            form.save()
            messages.success(request, "Resume Uploaded Successfully")
            return redirect('home')

        # return HttpResponseRedirect()


class CandidateView(View):

    def get(self, request, pk):

        candidate = Resume.objects.get(id=pk)

        messages.warning(request, "On Profile Info Page")
        return render(request,
                      'res_app/candidate.html',
                      {'candidate': candidate})


# subject = 'welcome to GFG world'
# message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [user.email, ]
# send_mail( subject, message, email_from, recipient_list )
