from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():

            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            msg = request.POST.get('msg')

            email_message = EmailMessage(
                'Support ticket from FutbolWebApp',
                'User: {}\nEmail: {}\nSubject: {}\nMessage: {}'.format(name,email,subject,msg),
                "",["danarv1412@gmail.com"],reply_to=[email])
            
            try:
                email_message.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?no-valid")

    return render(request, 'contact.html', {'contactForm':contact_form})