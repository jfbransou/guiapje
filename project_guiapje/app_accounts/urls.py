from django.contrib.auth import views
from django.urls import path, re_path, include
from project_guiapje import settings
from project_guiapje.app_accounts import views as views_accounts

app_name = 'app_accounts'

urlpatterns = [
    #re_path(r'^$', views.home, name='home'),
    #re_path(r'^$',views.home,name='home'),
    
    re_path(r'^conta/$', views_accounts.dashboard,name='dashboard'),
    
    re_path(r'^entrar/$',views.LoginView.as_view(template_name='app_accounts/login.html'),name='login'),

    re_path(r'^cadastre-se/$',views_accounts.register,name='register'),
    re_path(r'^sair/$',views_accounts.logout,name='logout'),
    re_path(r'^editar/$',views_accounts.edit,name='edit'),
    re_path(r'^editar-senha/$',views_accounts.edit_password,name='edit_password'),
    
    re_path(r'^nova-senha/$',views_accounts.password_reset,name='password_reset'),
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$',views_accounts.password_reset_confirm,name='password_reset_confirm'),

]
