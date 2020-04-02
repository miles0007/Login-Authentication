from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include, url
from app import views


urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login_fun,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_request,name='logout'),
    path('premium/',views.premium,name='pro')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












