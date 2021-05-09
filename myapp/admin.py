from django.contrib import admin
from myapp.models import level3data , level2data,level1data ,level4data,level5data,level6data,answers,FinalScore,userInfo,clickedImages

# Register your models here.
admin.site.register(level1data)
admin.site.register(level2data)
admin.site.register(level3data)
admin.site.register(level4data)
admin.site.register(level5data)
admin.site.register(level6data)
admin.site.register(answers)
admin.site.register(FinalScore)
admin.site.register(userInfo)
admin.site.register(clickedImages)


