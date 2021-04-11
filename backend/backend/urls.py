"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from ArticlesApp import views as ArticlesAppView
from UsersApp import views as UsersAppView
from rest_framework_simplejwt import views as jwt_views
# from rest_framework.authtoken.views import obtain_auth_token



# Myuser, Badge, Tribut, Child, Trophies, TutorLink
router = routers.DefaultRouter()
router.register(r'Articles', ArticlesAppView.ArticleView, 'Article')
router.register(r'Bibliographys', ArticlesAppView.BibliographyView, 'Bibliography')
router.register(r'Equipments', ArticlesAppView.EquipmentView, 'Equipment')
router.register(r'Images', ArticlesAppView.ImageView, 'Image')
router.register(r'ListImages', ArticlesAppView.ListImageView, 'ListImage')
router.register(r'ListEquipments', ArticlesAppView.ListEquipmentView, 'ListEquipment')
router.register(r'ListVideos', ArticlesAppView.ListVideoView, 'ListVideo')
router.register(r'Videos', ArticlesAppView.VideoView, 'Video')

router.register(r'Userss', UsersAppView.UsersView, 'Users')
router.register(r'Badges', UsersAppView.BadgeView, 'Badge')
router.register(r'Tributs', UsersAppView.TributView, 'Tribut')
router.register(r'Childs', UsersAppView.ChildView, 'Child')
router.register(r'Trophiess', UsersAppView.TrophiesView, 'Trophies')
router.register(r'TutorLinks', UsersAppView.TutorLinkView, 'TutorLink')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('UsersApp.urls')),
]
