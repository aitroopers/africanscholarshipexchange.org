# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.shortcuts import redirect
# Create your views here.

def contact(requests):
    form = ContactForm
    website_name = "African Scholarship Exchange"
    title = "ASE | Contact Us"
    ase_summary = "ASE partners with African churches and organizations to identify future leaders and equip them with the education they need to succeed."
    page = {"title": " Contact Us", "name": "Contact"}

    # new logic!
    if requests.method == 'POST':
        form = form(data=requests.POST)

        if form.is_valid():
            name = requests.POST.get('name', '')
            email = requests.POST.get('email', '')
            number = requests.POST.get('number', '')
            subject = requests.POST.get('subject', '')
            message = requests.POST.get('message', '')

            # Email the profile with the
            # contact information
            template =get_template('contact/contact_template.txt')
        context = {
            'name': name,
            'email': email,
            'number':number,
            'subject':subject,
            'message': message,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "ASE" + '',
            ['aitroopers@gmail.com'],
            headers={'Reply-To': email}
        )
        email.send()
        return redirect('/contact')


    return render(requests,  "contact/index.html",locals())








