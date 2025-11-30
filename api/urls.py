from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# urlpatterns = [
#     path('products/', get_products)
# ]

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = router.urls

# urlpatterns = [
#     path('user/', UserProfileAPIView.as_view()),
#     path('user/register/', RegisterAPIView.as_view()),
#     path('user/login/', LoginAPIView.as_view()),
# ]

# urlpatterns = [
#     path('list/', ProductListAPIView.as_view()),
#     path('create/', ProductCreateAPIView.as_view()),
#     path('detail/<int:pk>/', ProductDetailAPIView.as_view()),
#     path('delete/<int:pk>/', ProductDeleteAPIView.as_view()),
#     path("update/<int:pk>/", ProductUpdateAPIView.as_view())
# ]

#
# urlpatterns = [
#     path("test/<str:name>/", TestAPI.as_view(), name='test'),
#     path('get/', ProductListView.as_view(), name='all-products'),
#     path('create/', ProductCreateView.as_view(), name='create-product'),
#
#     path("all-products/", get_products),
#     path('create-products/', create_product),
#
#     path('crud/get/', ProductGETAPIView.as_view()),
#     path('crud/put/<int:pk>/', ProductPUTAPIView.as_view()),
#     path('crud/patch/<int:pk>/', ProductPATCHAPIView.as_view()),
#     path('crud/delete/<int:pk>/', ProductDELETEAPIView.as_view()),
# ]
#
#
