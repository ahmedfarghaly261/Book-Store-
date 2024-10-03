from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.book,name="books"),
    path("section_books",views.sec_books,name="sec_books"),
    path("login",views.user,name="login"),
    path('book_content/<str:book_name>/', views.book_content, name='book_content'),
    path('cart/<str:bookName>/',views.cart, name='cart')

]
