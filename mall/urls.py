from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mall import views

app_name = 'mall'

urlpatterns = [
  path('', views.product_in_category, name='product_all'),
  path('<category_slug>/', views.product_in_category, name='product_in_category'),
  path('<int:id>/<product_slug>/', views.product_detail, name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)