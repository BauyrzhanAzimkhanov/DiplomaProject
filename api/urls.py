from django.urls import path

# from rest_framework_jwt.views import obtain_jwt_token

from api.views import SemesterListAPIView, SemesterDetailAPIView, CourseListAPIView, CourseDetailAPIView, UserListAPIView, UserDetailAPIView, LectureListAPIView, LectureDetailAPIView, AbsenceOrLateListAPIView, AbsenceOrLateDetailAPIView, WorkListAPIView, WorkDetailAPIView, WorkMaterialListAPIView, WorkMaterialDetailAPIView, MarkListAPIView, MarkDetailAPIView

urlpatterns = [
    # CBV

    path('semesters/', SemesterListAPIView.as_view()),
    path('semesters/<int:pk>/', SemesterDetailAPIView.as_view()),

    path('courses/', CourseListAPIView.as_view()),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view()),

    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),

    path('lectures/', LectureListAPIView.as_view()),
    path('lectures/<int:pk>/', LectureDetailAPIView.as_view()),

    path('absences_or_lates/', AbsenceOrLateListAPIView.as_view()),
    path('absences_or_lates/<int:pk>/', AbsenceOrLateDetailAPIView.as_view()),

    path('works/', WorkListAPIView.as_view()),
    path('works/<int:pk>/', WorkDetailAPIView.as_view()),

    path('work_materials/', WorkMaterialListAPIView.as_view()),
    path('work_materials/<int:pk>/', WorkMaterialDetailAPIView.as_view()),

    path('marks/', MarkListAPIView.as_view()),
    path('marks/<int:pk>/', MarkDetailAPIView.as_view()),

]
