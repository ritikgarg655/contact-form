from django.urls import path
from .views import create_form,view,view_id

app_name = "contact_form"
urlpatterns = [
	path("create_form/",create_form),
	path("view/",view),
	path("view/<int:my_id>",view_id),
]