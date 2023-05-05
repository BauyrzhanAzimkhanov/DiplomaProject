from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Semester(models.Model):
    name = models.CharField(max_length=20)
    startingDate = models.DateField()
    endingDate = models.DateField()

    class Meta:
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'
    
    def __str__(self):
        return f'{self.id}: {self.name} starting at {self.startingDate.__str__} untill {self.endingDate.__str__}'
    
class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, related_name='courses')
    courseCode = models.CharField(max_length=8)
    description = models.TextField(default='')
    prerequisites = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='subPrerequisites')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'{self.id}: {self.courseCode}'

class User(models.Model):
    kbtuId = models.CharField(max_length=10)
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    yearOfStudy = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(7)])
    isTeacher = models.BooleanField(default=False)
    isAssistant = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    gpa = models.FloatField(default=1.0, validators=[MinValueValidator(1.0), MaxValueValidator(4.0)])
    finishedCourses = models.ManyToManyField(Course, on_delete=models.CASCADE, null=True, related_name='courseFinishedUsers')
    studyingCourse = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='courseStudyingUser')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.firstName} {self.lastName} : id={self.kbtuId}'

class Lecture(models.Model):
    theme = models.TextField('')
    topics = models.TextField('')
    studyWeek = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(16)])
    date = models.DateField()
    startingTime = models.TimeField()
    endingTime = models.TimeField()
    classRoom = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='lectures')
    isLecture = models.BooleanField(default=False)
    isPractice = models.BooleanField(default=False)
    isMidterm = models.BooleanField(default=False)
    isFinal = models.BooleanField(default=False)
    isFX = models.BooleanField(default=False)
    isQuiz = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Lecture'
        verbose_name_plural = 'Lectures'

    def __str__(self):
        return f'{self.id}: {self.studyWeek} | {self.course}'

class AbsenceOrLate(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='absencesOrLates')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, related_name='absentOrLateStudents')
    isAbsence = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Absence or late'
        verbose_name_plural = 'Absences or lates'

    def __str__(self):
        return f'{self.id}: '

class Work(models.Model):
    topic = models.TextField('')
    description = models.TextField('')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, related_name='works')
    startDate = models.DateField()
    deadlineDate = models.DateField()
    startingTime = models.TimeField()
    endingTime = models.TimeField()
    isHomeWork = models.BooleanField(default=False)
    isLecture = models.BooleanField(default=False)
    isPractice = models.BooleanField(default=False)
    isMidterm = models.BooleanField(default=False)
    isFinal = models.BooleanField(default=False)
    isFX = models.BooleanField(default=False)
    isQuiz = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return f'{self.id}: {self.topic}'

class WorkMaterial(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, related_name='workMaterial')
    binData = models.BinaryField()

    class Meta:
        verbose_name = 'Work material'
        verbose_name_plural = 'Work materials'

    def __str__(self):
        return f'{self.id}: {self.work}'

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='marks')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, related_name='marks')
    workMark = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'

    def __str__(self):
        return f'{self.id}: {self.work} - {self.workMark}'
