from django.urls import path
from .views import CertificadoModularList, CertificadoModularDetail

app_name = "certificados"

urlpatterns = [
    path("listcm/", CertificadoModularList.as_view(), name = "list_cm"),
    path("detailcm/<pk>/", CertificadoModularDetail.as_view(), name = "single_cm"),
]
