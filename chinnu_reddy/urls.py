from django.urls import path
from chinnu_reddy import views
urlpatterns =[
path('rt/',views.home,name="home"),
path('demo/',views.chk),
path('hm/',views.homepage),
path('lg/',views.lgn),
path('rg/',views.reg),
path('',views.bthm),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('registration/',views.registration,name="registration"),
path('cr/',views.crud,name="cr"),
path('del/<str:st>',views.deletedata,name="delete"),
path('df/',views.dform,name="dff"),
path('showdata/',views.showinfo,name="show"),
path('infodelete/<int:et>',views.infodelete,name="infodelete"),
# path('edit/<int:id>',views.edit,name="editdata"),
path('e/<int:si>/',views.userupdate,name="ue"),
path('ui/<str:username>/',views.userinfo,name="ufi"),

]

