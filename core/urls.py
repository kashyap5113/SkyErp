from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('overview/', views.product, name='overview'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('account/', views.account, name='account'),
    path('asset_management/', views.asset_management, name='asset_management'),
    path('buying/', views.buying, name='buying'),
    path('crm/', views.crm, name='crm'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hrms/', views.hrms, name='hrms'),
    path('manufacturing/', views.manufacturing, name='manufacturing'),
    path('projects/', views.projects, name='projects'),
    path('reports/', views.reports, name='reports'),
    path('selling/', views.selling, name='selling'),
    path('stock/', views.stock, name='stock'),
    path('support/', views.support, name='support'),
    path('schedule_demo/', views.schedule_demo, name='schedule_demo'),
    path('schedule_demo/index', RedirectView.as_view(pattern_name='schedule_demo', permanent=True)),
]
