from django.urls import path

# from rest_framework_jwt.views import obtain_jwt_token

from api.views import *

urlpatterns = [
    # path('login/', obtain_jwt_token),

    # FBV
    # path('categories/', category_list),
    # path('categories/<int:pk>/', category_detail),

    # path('products/', product_list),
    # path('products/<int:pk>/', product_detail),

    # path('shipping/', shipping_list),
    # path('shipping/<int:pk>/', shipping_detail),

    # path('images/', image_list),
    # path('images/<int:pk>/', image_detail),

    # path('comments/', comment_list),
    # path('comments/<int:pk>/', comment_detail),

    # CBV
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),

    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),

    path('courses/', CourseListAPIView.as_view()),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view()),

    path('lectures/', LectureListAPIView.as_view()),
    path('lectures/<int:pk>/', LectureDetailAPIView.as_view()),

    path('absences/', AbsencesListAPIView.as_view()),
    path('absences/<int:pk>/', AbsencesDetailAPIView.as_view()),

    path('lates/', LatesListAPIView.as_view()),
    path('lates/<int:pk>/', LatesDetailAPIView.as_view()),

    path('marks/', MarksListAPIView.as_view()),
    path('marks/<int:pk>/', MarksDetailAPIView.as_view()),

    path('home_works/', HomeWorksListAPIView.as_view()),
    path('home_works/', HomeWorksDetailAPIView.as_view()),

    path('class_materials/', ClassMaterialsListAPIView.as_view()),
    path('class_materials/', ClassMaterialsDetailAPIView.as_view()),

    path('home_work_materials/', HomeWorkMaterialsListAPIView.as_view()),
    path('home_work_materials/', HomeWorkMaterialsDetailAPIView.as_view()),


    # path('shipping/', ShippingListAPIView.as_view()),
    # path('shipping/<int:pk>/', ShippingDetailAPIView.as_view()),
    #
    # path('images/', ImageListAPIView.as_view()),
    # path('images/<int:pk>/', ImageDetailAPIView.as_view()),
    #
    # path('comments/', CommentListAPIView.as_view()),
    # path('comments/<int:pk>/', CommentDetailAPIView.as_view()),
]
