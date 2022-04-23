from django.urls import path
from Categories import views


urlpatterns = [
    #Category part
    path('categories/', views.CategoriesViewSet.as_view(), name='categories'),
    path('categories_update_delete/<int:pk>/', views.CategoriesUpdateDelete.as_view(), name='categories_update_delete'),
    #Sub Category part
    path('sub_categories/', views.SubCategoriesViewSet.as_view(), name='sub_categories'),
    path('sub_categories_update_delete/<int:pk>/', views.SubCategoriesUpdateDelete.as_view(),name='sub_categories_update_delete'),

]
