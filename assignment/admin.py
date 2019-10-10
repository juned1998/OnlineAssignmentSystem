from django.contrib import admin
from assignment.models import Student , Faculty ,Assignment ,Course , Question ,Answer,StudyYear ,Branch, Semester
# Register your models here.
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudyYear)
admin.site.register(Branch)
admin.site.register(Semester)
