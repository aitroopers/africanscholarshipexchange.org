# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import About, TeamMember, Location
from students.models import Student
from random import randint
# Create your views here.


def home(requests):
    title = "ASE | Home"
    website_name = "African Scholarship Exchange"
    about = About.objects.get(id=1)
    ase_summary = about.summary_text
    ase_about = about.description_text
    tag_line = about.tag_line
    why_choose_us = [{'title': "Scholarship",
                      "content": "African Scholarship Exchange is a scholarship ministry with a unique approach."},
                     {'title': "Ministry",
                      "content": "Our scholarship ministry for African students is rooted in the love of Christ."},
                     {'title': "Support",
                      "content": "African Scholarship Exchange is a scholarship ministry with a unique approach. It's not just about giving money to someone."}, ]
    what_we_do = [
        {'title': "Who We Are", "bg_img": "images/WhoWeAre2.jpg", "link": "/about",
         "content": "Founded in 1997, ASE is a scholarship ministry with a unique approach. By funding educational opportunities in Africa, we have served over 800 men and women with university degrees and beyond in all fields of study."},
        {'title': "Student Stories", "bg_img": "images/addy2.png", "link": "/students",
         "content": "Our alumni have unique, exciting life stories to share with our supporters. ASE not only provides financial support. Every student develops a relationship with us through our partners in their home country."},
        {'title': "Pray, Give, Go", "bg_img": "images/service-6.jpg", "link": "/donate/",
         "content": "Get involved with ASE. Pray with us for the ministry and for Africa. If you want to pray for and sponsor a specific students, contact us. Share our website. Connect with us on social media. Ask us about ways to donate."},
    ]

    page = {"title": " Home", "name": ""}

    student = Student.objects.get(id=randint(1, 10))
    return render(requests, "home/index.html", locals())


def about(requests):
    website_name = "African Scholarship Exchange"
    title = "ASE | About Us"
    about = About.objects.get(id=1)
    ase_summary = about.summary_text
    ase_about = about.description_text
    quotes = [
        "We believe the Bible to be the inspired, the only infallible, authoritative Word of God.",
        "We believe that there is one God, eternally existent in three persons; Father, Son, and Holy Spirit.",
        "We believe in the resurrection of both the saved and the lost; they that are saved unto the resurrection of life, and they that are lost unto the resurrection of damnation.",
        "We believe that for the salvation of lost and sinful man regeneration by the Holy Spirit is absolutely essential.",
        "We believe in the present ministry of the Holy Spirit by whose indwelling the Christian is enabled to live a godly life.",
        "We believe in the spiritual unity of believers in Christ."
    ]

    locations = Location.objects.all()

    team = TeamMember.objects.all()[:3]
    page = {"title":" About Us", "name":"About"}

    return render(requests, "about/index.html", locals())




