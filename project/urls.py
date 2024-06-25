from django.urls import path

from . import views

urlpatterns = [
    path('get_balance/', views.get_balance_view, name='get_balance'),
    path('get_balance_batch/', views.get_balance_batch_veiw, name='get_balance_batch'),
    path('get_token_info/', views.get_token_info_view, name='get_token_info'),
]