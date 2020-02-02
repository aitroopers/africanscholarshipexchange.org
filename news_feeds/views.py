# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def news_feeds(requests):
    content = """
    A non-profit organization (NPO), also known as a non-business entity[1] or non-profit institution,[2] is dedicated to furthering a particular social cause or advocating for a shared point of view. In economic terms, it is an organization that uses its surplus of the revenues to further achieve its ultimate objective, rather than distributing its income to the organization's shareholders, leaders, or members. Non-profits are tax exempt or charitable, meaning they do not pay income tax on the money that they receive for their organization. They can operate in religious, scientific, research, or educational settings.

    The key aspects of nonprofits is accountability, trustworthiness, honesty, and openness to every person who has invested time, money, and faith into the organization. Nonprofit organizations are accountable to the donors, funders, volunteers, program recipients, and the public community. Public confidence is a factor in the amount of money that a nonprofit organization is able to raise. The more nonprofits focus on their mission, the more public confidence they will have, and has a result, more money for the organization.[1] The activities a nonprofit is partaking in can help build the public’s confidence in nonprofits, as well as how ethical the standards and practices are.
    """
    website_name = "African Scholarship Exchange"
    title = "ASE | News Events"
    ase_summary = "ASE partners with African churches and organizations to identify future leaders and equip them with the education they need to succeed."


    page = {"title": " News Events", "name": "News Events"}


    blog_list = News.objects.all()

    paginator = Paginator(blog_list, 4)

    current_page = requests.GET.get('page')

    if current_page:
        blogs = paginator.page(int(current_page))
        return render(requests, "news_events/index.html", locals())

    else:
        current_page = requests.GET.get('blog')
        blog = News.objects.get(id=int(current_page))
        return render(requests, 'news_events/single_news.html', locals())
