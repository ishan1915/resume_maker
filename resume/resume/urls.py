from django.contrib import admin 
from django.urls import path 
from createres.views import *

urlpatterns = [ 
	path('', home, name = 'createres'), 
	path('resume/', gen_resume, name = 'resume'), 
	path("admin/", admin.site.urls), 
] 
