from django.urls import path
from django.contrib.auth import views as auth_views  # Importamos las vistas de autenticación de Django
from .views import FacturaListView, FacturaDetailView

urlpatterns = [
    # Rutas para las facturas
    path('facturas/', FacturaListView.as_view(), name='facturas-list'),
    path('facturas/<int:pk>/', FacturaDetailView.as_view(), name='factura-detail'),

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='factura/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
