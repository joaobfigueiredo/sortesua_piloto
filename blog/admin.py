from django.contrib import admin
from blog.models import Post, Category
from sortesua.models import Aposta

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
	
class ApostaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Aposta, ApostaAdmin)