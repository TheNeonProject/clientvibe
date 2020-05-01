"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from releases.views import PostmarkWebhook, FeedbackView, SendReleaseView


urlpatterns = [
    path(
        'send/<int:release_id>/',
        SendReleaseView.as_view(),
        name='send_release'
    ),
    path(
        'postmark/<str:project_slug>/',
        PostmarkWebhook.as_view(),
        name='postmark_webhook'
    ),
    path(
        'feedback/<uuid:release>/<str:email>/',
        FeedbackView.as_view(),
        name='feedback'
    ),
    path('admin/', admin.site.urls),
]
