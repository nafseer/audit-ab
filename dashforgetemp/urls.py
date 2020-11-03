"""dashforgetemp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from testapp.views import AnalyticsView,SalesView,UsersView,LoginView
from userprofile.views import UsersListView,UserSignUpView
from userroles.views import UserRolesListView,UserRolesCreateView
from django.contrib.auth import views as auth_views
from company.views import CompanysListView,CompanyListCreateView,CompanysDetailsView
from trailbalancemaster.views import TrailListView,TrailListCreateView
from leads.views import LeadsListView,LeadsListCreateView
from adjustments.views import AdjustmentListView,AdjustmentListCreateView
# from client.views import ClientsContactCreateView,ClientsListView,ClientsProfileListCreateView,ClientsTeamListCreateView
from programs.views import ProgramListCreateView,ProgramListView
from procedure.views import ProcedureCreateView,CommentCreateView,ProceduresListView
from client.views import ClientsListView,ClientsProfileListCreateView,ClientsTeamListCreateView,ClientsContactCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='page-signin.html'),name= 'home'),
    path('', auth_views.LoginView.as_view(), name='login'),

    path('webanalytics',AnalyticsView.as_view(template_name='dashboard-two.html'), name='webanalytics'),

    #Users Details
    path('userslist',UsersListView.as_view(), name='userslist'),

    #Login in web templates
    # path('', auth_views.LoginView.as_view(template_name='page-signin.html'),name='login'),
   
   #Logout in template
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),

    #Home View Login
    path('home', TemplateView.as_view(template_name='dashboard-one.html'), name='home'), 

    #add users in template admin
    path('useradd/', UserSignUpView.as_view(), name='useradd'),

    #User Roles Details
    path('userroles', UserRolesListView.as_view(), name='userroles'),

    #User Roles Create Details
    path('userrolescreate', UserRolesCreateView.as_view(), name='userrolescreate'),

    #Company Details
    path('companylist', CompanysListView.as_view(), name='companylist'),

    #Companys List Create 
    path('companylistcreate', CompanyListCreateView.as_view(), name='companylistcreate'),

    #Companys Info And Details Details  
    path('companydetails/<int:pk>/', CompanysDetailsView.as_view(), name='companydetails'),

    #Program Details
    path('programlist', ProgramListView.as_view(), name='programlist'),

    #User Roles Create 
    path('programlistcreate', ProgramListCreateView.as_view(), name='programlistcreate'),

    #Trail List Details
    path('traillist', TrailListView.as_view(), name='traillist'),

    #User Roles Create Details
    path('traillistcreate', TrailListCreateView.as_view(), name='traillistcreates'),
 
    #Leads List Details
    path('leadslist', LeadsListView.as_view(), name='leadslist'),

    #Leads Roles Create Details
    path('leadslistcreate', LeadsListCreateView.as_view(), name='leadslistcreate'),

    #Adjustment List Details
    path('adjustmentlist', AdjustmentListView.as_view(), name='adjustmentlist'),

    #Adjustment List Create Details
    path('adjustmentlistcreate', AdjustmentListCreateView.as_view(), name='adjustmentlistcreate'),

    #Clients Details
    path('clients', ClientsListView.as_view(), name='clients'),

    #Clients Profile List Create
    path('companydetails/<int:pk>/clientsprofilecreate', ClientsProfileListCreateView.as_view(), name='clientsprofilecreate'),

    #Clients Team List Create
    path('companydetails/<int:pk>/clientsteamcreate', ClientsTeamListCreateView.as_view(), name='clientsteamcreate'),

    #Clients Conact List Create
    path('companydetails/<int:pk>/clientscontactcreate', ClientsContactCreateView.as_view(), name='clientscontactcreate'),

    #Procedures List Create
    path('companydetails/<int:pk>/procedureslistcreate', ProcedureCreateView.as_view(), name='procedureslistcreate'),

    # Procedures view 
    # path('companydetails/<int:pk>/procedureslist', ProceduresListView.as_view(), name='procedureslist'),

    #Procedures comment view 
    path('companydetails/<int:pk>/procedurescomment', CommentCreateView.as_view(), name='procedurescomment'),

    #Procedures list view 
    path('companydetails/<int:pk>/procedures', ProceduresListView.as_view(), name='procedureslist'),
    # #Procedure List view 
    # path('companydetails/<int:pk>/procedurelist', ProcedureListView.as_view(), name='procedurelist'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

