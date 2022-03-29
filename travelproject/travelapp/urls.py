#from django.conf.urls.static import static
#from travelproject import settings
from .import views
from django.urls import path




urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('',include('travelapp.urls'))
    path('',views.demo,name='demo')
    #path('add/',views.addition,name='addition')
    #path('add/',views.addition,name='addition'),
    #path('sub/',views.subtraction,name='subtraction')


    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thankyou/',views.thankyou,name='thankyou')
]
