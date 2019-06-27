from django.conf.urls import url
from .hr_api import *

urlpatterns = [
    url(r"^register$", AddStaffAPIView.as_view()),
    url(r"^delete$", DeleteStaffAPIView.as_view()),
    url(r"^staff_info$", StaffInfoAPIView.as_view()),
]