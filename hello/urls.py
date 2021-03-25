from django.urls import Path
from . import views
urlpatterns=[
    Path("",views.index, name="index")

]