from django.contrib import admin
from .models import Users
from .models import UserProfile,Global,ProfilePicture,QuizReg#,QuizGlobal

admin.site.register(Users)
admin.site.register(UserProfile)
admin.site.register(Global)
admin.site.register(ProfilePicture)
admin.site.register(QuizReg)
#admin.site.register(QuizGlobal)