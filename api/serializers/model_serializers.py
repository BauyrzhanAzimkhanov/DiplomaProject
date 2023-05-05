from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from api.models.models import Semester, Course, User, Lecture, AbsenceOrLate, Work, WorkMaterial, Mark

class SemesterSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Semester
        fields = ('id', 'name', 'startingDate', 'endingDate', 'courses')

class SubPrerequisites(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseCode', 'description')

class CourseSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer(many=True, read_only=True)
    prerequisites = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    subPrerequisites = serializers.SubPrerequisites(many=True, read_only=True)
    courseFinishedUsers = serializers.ManyRelatedField(many=True, read_only=True)
    courseStudyingUser = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    lectures = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ('id', 'semester', 'courseCode', 'description', 'prerequisites', 'courseFinishedUsers', 'courseStudyingUser', 'lectures')

class UserSerializer(serializers.ModelSerializer):
    finishedCourses = serializers.ManyRelatedField(many=True, read_only=True)
    studyingCourse = CourseSerializer(many=True, read_only=True)
    marks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    absencesOrLates = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'kbtuId', 'firstName', 'middleName', 'lastName', 'yearOfStudy', 'isTeacher', 'isAssistant', 'isAdmin', 'gpa', 'finishedCourses', 'studyingCourse', 'marks', 'absencesOrLates')

class LectureSerializer(serializers.ModelField):
    course = CourseSerializer(many=True, read_only=True)
    absentOrLateStudents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    works = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'theme', 'topics', 'studyWeek', 'date', 'startingTime', 'endingTime', 'classRoom', 'course', 'isLecture', 'isPractice', 'isMidterm', 'isEndterm', 'isFinal', 'isFx', 'isQuiz', 'absentOrLateStudents', 'works')

class AbsenceOrLateSerializer(serializers.ModelField):
    student = UserSerializer(many=True, read_only=True)
    lecture = LectureSerializer(many=True, read_only=True)


    class Meta:
        model = AbsenceOrLate
        fields = ('id', 'student', 'lecture', 'isAbsence')

class WorkSerializer(serializers.ModelField):
    lecture = LectureSerializer(many=True, read_only=True)
    workMaterial = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    marks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Work
        fields = ('id', 'topic', 'description', 'lecture', 'startDate', 'deadlineDate', 'startingTime', 'endingTime', 'isHomeWork', 'isLecture', 'isPractice', 'isMidterm', 'isEndterm', 'isFinal', 'isFx', 'isQuiz', 'workMaterial', 'marks')

class WorkMaterialSerializer(serializers.ModelField):
    work = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = WorkMaterial
        fields = ('id', 'work', 'binData')

class MarkSerializer(serializers.ModelField):
    student = UserSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Mark
        fields = ('id', 'student', 'work', 'workMark')
