from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Discipline(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=8)
    description = models.TextField(default='')
    
    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'
    
    def __str__(self):
        return f'{self.id}: {self.code} | {self.name} - {self.description}.'

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
    absenceCount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(72)])
    finishedCourses = models.ManyToManyField(Discipline, on_delete=models.CASCADE, null=True, related_name='finishedCources')
    studyingCourseCode = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True, related_name='studyingCourseCode')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.firstName} {self.lastName} : id={self.kbtuId}'

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
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, related_name='semester')
    courseCode = models.CharField(max_length=8)
    descritpion = models.TextField(default='')
    prerequisites = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='prerequisites')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'{self.id}: {self.courseCode}'

class Lecture(models.Model):
    theme = models.TextField('')
    topics = models.TextField('')
    studyWeek = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(16)])
    date = models.DateField()
    startingTime = models.TimeField()
    endingTime = models.TimeField()
    classRoom = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='course')
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

class Absence(models.Model):
    students = models.ManyToManyField(User, on_delete=models.CASCADE, null=True, related_name='students')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, related_name='lectures')
    

    class Meta:
        verbose_name = 'Absence'
        verbose_name_plural = 'Absence'

    def __str__(self):
        return f'{self.id}: '
