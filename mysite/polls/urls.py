# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 08:39:47 2015

@author: Kevin
"""

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
        url(r'^hello', views.index, name='index'),
        url(r'^look', views.look, name='look'))
