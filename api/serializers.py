from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.reverse import reverse
from api.models import Product, Category
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    detail_link = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'detail_link', 'price', 'discount_price', 'description', 'category', 'category_id', 'image']

    def get_discount_price(self, obj):
        return obj.price - obj.price * 0.2

    def get_detail_link(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/api/products/{obj.id}/")
        return f'/api/products/{obj.id}/'

    def validate_image(self, value):
        if value.size > 0.2 * 1024 * 1024:
            raise ValidationError("Rasm hajmi 200kB dan oshmasligi kerak...")
        return value



    # def validate(self, attrs):  # attrs == request.data
    #     if attrs['price'] < 0:
    #         raise serializers.ValidationError("Narx musbat son bo'lishi kerak")
    #     return attrs


    # def validate_fieldname(self, value):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Narx musbat son bo'lishi kerak")
        return value

    def validate_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Maxsulot nomi 3 tadan uzun bo'lsin")
        return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['limit'] = 1000
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'last_name', 'first_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.FloatField()
#     description = serializers.CharField()
#
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
