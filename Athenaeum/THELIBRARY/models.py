from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    title=models.CharField(max_length=120,unique=True)
    price=models.IntegerField(default=200)
    author=models.CharField(max_length=120)

    def __str__(self):
        return self.title

    def average_rating(self):
        reviews=self.reviews_set.all()
        if reviews:
            rating=[r.rating for r in reviews]
            total=sum(rating)
            return total/len(reviews)
        else:
            return 0
    def total_reviews(self):
        return self.reviews_set.all().count()

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    reviews=models.CharField(max_length=120)
    rating=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return self.reviews
class Carts(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ("incart","incart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="incart")

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE)

    options = (
        ("order-placed", "order-placed"),
        ("dispatched","dispatched"),
        ("cancelled", "cancelled"),
    )
    status=models.CharField(max_length=120,choices=options,default="incart")




