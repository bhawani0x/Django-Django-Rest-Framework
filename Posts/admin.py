from django.contrib import admin
from .models import Post, Vote, Like, Choice, Topic, LikeCount, VoteCount
# Register your models here.
# admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(Like)
admin.site.register(LikeCount)
admin.site.register(Topic)
admin.site.register(VoteCount)


class ChoiceInline(admin.TabularInline):
# class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class PostAdmin(admin.ModelAdmin):
    # list_display = ["question_text", "pub_date"]
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    # ]
    inlines = [ChoiceInline]


admin.site.register(Post, PostAdmin)
