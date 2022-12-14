from django.contrib import admin
from cv.models import Skills, Internships, diploma
from cv.models import Language
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau','formation', 'language','dateS')
    list_filter = ('nom', 'niveau')
    date_hierarchy = 'dateS'
    ordering = ('dateS',)
    search_fields = ('nom', 'niveau') 
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'description',)
    list_filter = ('language', 'id')
    search_fields = ('language', 'niveau')
class diplomaAdmin(admin.ModelAdmin):
    list_display = ('MyEducation', 'MyExperience','dateD')
    list_filter = ('MyEducation', 'MyExperience')
    date_hierarchy = 'dateD'
    ordering = ('dateD',)
    search_fields = ('myEducation', 'dateD') 
class InternshipsAdmin(admin.ModelAdmin):
    list_display = ('namesociete', 'projet','dateI')
    list_filter = ('namesociete', 'projet')
    date_hierarchy = 'dateI'
    ordering = ('dateI',)
    search_fields = ('namesociete', 'dateI') 
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Internships, InternshipsAdmin)
admin.site.register(diploma, diplomaAdmin)