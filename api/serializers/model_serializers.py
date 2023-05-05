from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from api.models import Semester, Course, User, Lecture, AbsenceOrLate, Work, WorkMaterial, Mark

class SemesterSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Semester
        fields = ('id', 'name', 'startingDate', 'endingDate', 'courses')

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'semester', 'courseCode', 'description', 'prerequisiteList', 'courseFinishedUsers', 'courseStudyingUsers', 'lectures')
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'kbtuId', 'firstName', 'middleName', 'lastName', 'yearOfStudy', 'isTeacher', 'isAssistant', 'isAdmin', 'gpa', 'finishedCourses', 'studyingCourse', 'marks', 'absencesOrLates')

class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ('id', 'theme', 'topics', 'studyWeek', 'date', 'startingTime', 'endingTime', 'classRoom', 'course', 'isLecture', 'isPractice', 'isMidterm', 'isEndterm', 'isFinal', 'isFx', 'isQuiz', 'absentOrLateStudents', 'works')

class AbsenceOrLateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbsenceOrLate
        fields = ('id', 'student', 'lecture', 'isAbsence')

class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ('id', 'topic', 'description', 'lecture', 'startDate', 'deadlineDate', 'startingTime', 'endingTime', 'isHomeWork', 'isLecture', 'isPractice', 'isMidterm', 'isEndterm', 'isFinal', 'isFx', 'isQuiz', 'workMaterial', 'marks')

class WorkMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkMaterial
        fields = ('id', 'work', 'file')

class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = ('id', 'student', 'work', 'workMark')
