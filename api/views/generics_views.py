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

class ListAPIView(generics.ListCreateAPIView):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = Lecture.object.all()
    serializer_class = LectureSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.object.all()
    serializer_class = LectureSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = AbsenceOrLate.object.all()
    serializer_class = AbsenceOrLateSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AbsenceOrLate.object.all()
    serializer_class = AbsenceOrLateSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = Work.object.all()
    serializer_class = WorkSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.object.all()
    serializer_class = WorkSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = WorkMaterial.object.all()
    serializer_class = WorkMaterialSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkMaterial.object.all()
    serializer_class = WorkMaterialSerializer

class ListAPIView(generics.ListCreateAPIView):
    queryset = Mark.object.all()
    serializer_class = MarkSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.object.all()
    serializer_class = MarkSerializer
