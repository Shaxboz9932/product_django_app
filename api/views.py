from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.models import Product
from api.serializers import ProductSerializer, UserProfileSerializer, RegisterSerializer, LoginSerializer
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework import viewsets
from api.permissions import IsOwner
from rest_framework_simplejwt.views import TokenObtainPairView
from api.pagination import MyPagination, MyLOPagination, MyCursorPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

# @method_decorator(cache_page(60*2), name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    throttle_classes = [AnonRateThrottle]
    parser_classes = [MultiPartParser, FormParser]

    

@api_view(['GET'])
def get_products(request):
    key = 'products'
    data = cache.get(key)
    print(10/0)

    if data is None:
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        cache.set(key, data, 60*5)
        print("DBdan oldim")

    else:
        print("Cache dan oldim")

    return Response(data)


    @action(methods=['get'], detail=True)
    def discount(self, request, pk=None):
        product = self.get_object()
        discount = product.price - product.price * 0.2
        return Response({'discount': discount})

class UserProfileAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        })

    # def get_queryset(self):
    #     user = User.objects.filter(username=self.request.user)
    #     return user

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register_page'

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

# class ProductViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     def partial_update(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     def destroy(self, request, pk):
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return Response({"message": "Maxsulot o'chirildi"})

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductDeleteAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


#
# class ProductGETAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
# class ProductPUTAPIView(APIView):
#     def put(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
# class ProductPATCHAPIView(APIView):
#     def patch(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
# class ProductDELETEAPIView(APIView):
#     def get(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return Response({"message": "Maxsulot o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(["GET"])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
# @api_view(["POST"])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
#
# class TestAPI(APIView):
#
#     def get(self, request, name):
#         return Response({'data': name})
#
#
# class ProductListView(APIView):
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#
# class ProductCreateView(APIView):
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         errors = serializer.errors
#         formatted_errors = {}
#         for field, messages in errors.items():
#             formatted_errors[field] = messages[0]
#
#         return Response({"errors": serializer.errors})
#
#
