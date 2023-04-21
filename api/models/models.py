from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Shipping(models.Model):
    type = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'

    def __str__(self):
        return f'{self.id}: {self.type} - {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    short_description = models.TextField(default='')
    full_description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'


class Image(models.Model):
    url = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                related_name='images')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.id}'


class Comment(models.Model):
    sender = models.CharField(max_length=200)
    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                related_name='comments')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.id} - {self.sender}'

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
