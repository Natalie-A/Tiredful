# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

"""Tiredful_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url($', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url($', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  url(blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth.models import User, Group

from rest_framework import permissions, routers, serializers, viewsets


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


urlpatterns = [
    # URL for user login
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # URL for including intro app.
    path('', include('intro.urls', namespace="intro")),

    # URL for including library app
    path('api/v1/', include('library.urls', namespace="library-api")),
    path('library/', include('library.urls', namespace="library")),

    # URL for including exams app
    path('api/v1/', include('exams.urls', namespace="exams-api")),
    path('exams/', include('exams.urls', namespace="exams")),

    # URL for including blog app
    path('api/v1/', include('blog.urls', namespace="blog-api")),
    path('blog/', include('blog.urls', namespace="blog")),

    # URL for including trains app
    path('api/v1/', include('trains.urls', namespace="trains-api")),
    path('trains/', include('trains.urls', namespace="trains")),

    # URL for including health app
    path('api/v1/', include('health.urls', namespace="health-api")),
    path('health/', include('health.urls', namespace="health")),

    # URL for including advertisements app
    path('api/v1/', include('advertisements.urls', namespace="advertisements-api")),
    path('advertisements/', include('advertisements.urls', namespace="advertisements")),

]
