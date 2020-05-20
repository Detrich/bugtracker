from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('accounts/login/', views.loginuser),
    path('logout/', views.logoutuser),
    path('new/<int:userid>', views.createticket),
    path('ticket/<int:ticketid>', views.ticketdetail,name='detailpage'),
    path('ticket/<int:ticketid>/inprogress/<int:userid>', views.doticket),
    path('ticket/<int:ticketid>/done/<int:userid>', views.ticketdone),
    path('ticket/<int:ticketid>/edit/', views.editticket),
    path('ticket/<int:ticketid>/invalid/<int:userid>', views.invalidticket),
    path('user/<int:userid>', views.viewuser)
]
