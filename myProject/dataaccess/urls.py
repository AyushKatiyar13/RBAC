from django.urls import path
from .views import load_csv_to_db, access_data

urlpatterns = [
    path('load/', load_csv_to_db, name='load_csv_to_db'),
    path('access/', access_data, name='access_data'),
]
