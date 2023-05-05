from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.serializers.model_serializers import SemesterSerializer, CourseSerializer, UserSerializer, LectureSerializer, AbsenceOrLateSerializer, WorkSerializer, WorkMaterialSerializer, MarkSerializer
from api.models.models import Semester, Course, User, Lecture, AbsenceOrLate, Work, WorkMaterial, Mark


class SemesterListAPIView(generics.ListCreateAPIView):
    queryset = Semester.object.all()
    serializer_class = SemesterSerializer

class SemesterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.object.all()
    serializer_class = SemesterSerializer

class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class LectureListAPIView(generics.ListCreateAPIView):
    queryset = Lecture.object.all()
    serializer_class = LectureSerializer

class LectureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.object.all()
    serializer_class = LectureSerializer

class AbsenceOrLateListAPIView(generics.ListCreateAPIView):
    queryset = AbsenceOrLate.object.all()
    serializer_class = AbsenceOrLateSerializer

class AbsenceOrLateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AbsenceOrLate.object.all()
    serializer_class = AbsenceOrLateSerializer

class WorkListAPIView(generics.ListCreateAPIView):
    queryset = Work.object.all()
    serializer_class = WorkSerializer

class WorkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.object.all()
    serializer_class = WorkSerializer

class WorkMaterialListAPIView(generics.ListCreateAPIView):
    queryset = WorkMaterial.object.all()
    serializer_class = WorkMaterialSerializer

class WorkMaterialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkMaterial.object.all()
    serializer_class = WorkMaterialSerializer

class MarkListAPIView(generics.ListCreateAPIView):
    queryset = Mark.object.all()
    serializer_class = MarkSerializer

class MarkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.object.all()
    serializer_class = MarkSerializer
