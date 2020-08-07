from django.urls import path

from . import views

urlpatterns = [
    path('create',views.employee_create),
    path('employee',views.employee_read,name='read'),
    path('edit/<int:id>',views.employee_edit,name='edit'),
    path('update/<int:id>',views.employee_update,name='update'),
    path('delete/<int:id>',views.employee_delete,name='delete'),
]
