from django.contrib import admin

# Assuming you have this model
from .models import Project,Review,Tag

class ProjectAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

class ReviewAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

class TagAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Tag,TagAdmin)
