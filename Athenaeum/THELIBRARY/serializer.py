from rest_framework import serializers
from  THELIBRARY.models import Books,Reviews,Carts,Orders
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=[
            "first_name"
            "last_name"
            "username",
            "email",
            "password"
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
class BookSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    average_rating=serializers.CharField(read_only=True)
    total_reviews=serializers.CharField(read_only=True)
    class Meta:
        model=Books
        fields=[
            "id"
            "title",
            "price",
            "author",
            "average_rating",
            "total_reviews",
        ]
class ReviewSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Reviews
        fields=[
            "user","reviews","rating"
        ]
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")

class CartSerializer(serializers.ModelSerializer):

    users=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    quantity=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["users",
                "product",
                 "date",
                 "status",
                 "quantity"]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product,**validated_data)
class OrderSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=[
            "user",
            "product",
            "status"
        ]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Orders.objects.create(user=user,product=product,**validated_data)








