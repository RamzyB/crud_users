from django.urls import path
from .views import create, user_list, user_detail, user_update, user_delete

urlpatterns = [
    path('create/', create),
    path('users/', user_list),
    path('users/<int:id>', user_detail),
    path('userupdate/<int:id>', user_update),
    path('userdelete/<int:id>', user_delete)
]
