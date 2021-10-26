from contact import views
from django.urls import include, path

app_name = 'contact'

urlpatterns = [
    # new url definition
    path('contact/msg/', views.contact)
]
