from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from THELIBRARY.models import Books,Carts,Orders
from rest_framework import viewsets,status
from THELIBRARY.serializer import UserSerializer,BookSerializer,ReviewSerializer,CartSerializer,OrderSerializer
from rest_framework.decorators import action

class UserRegister(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class BookViewSets(viewsets.ModelViewSet):
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    queryset =Books.objects.all()

    @action(methods=["post"], detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.all()
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"product":book})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["get"], detail=True)
    def get_review(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            Book=Books.objects.get(id=id)
            review = Book.reviews_set.all()
            serializer = ReviewSerializer(review, many=True)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(methods=["post"], detail=True)
    def add_to_carts(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        user = request.user
        serializer=CartSerializer(data=request.data,context={"user":user,"product":book})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"], detail=True)
    def add_orders(self, request, *args, **kwargs):
            id = kwargs.get("pk")
            book = Books.objects.get(id=id)
            user = request.user
            serializer = OrderSerializer(data=request.data, context={"user": user, "product": book})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
class CartsView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(users=self.request.user)



