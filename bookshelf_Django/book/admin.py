from django.contrib import admin
from .models import Book
# Register your models here.
# 管理者画面で表示されるように登録する。
admin.site.register(Book)

