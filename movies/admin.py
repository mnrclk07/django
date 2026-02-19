from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_date", "isPublished")  # Admin panelinde hangi alanların görüneceğini belirler
    search_fields = ("name","description")  # Admin panelinde arama yaparken hangi alanlarda arama yapılacağını belirler
    list_filter = ("created_date",)  # Admin panelinde filtreleme yaparken hangi alanların kullanılacağını belirler
    list_display_links = ("id", "name")  # Admin panelinde hangi alanların tıklanabilir olduğunu belirler
    list_per_page = 20  # Admin panelinde sayfa başına kaç kayıt gösterileceğini belirler
    list_editable = ("isPublished",)  # Admin panelinde hangi alanların düzenlenebilir olduğunu belirler
# Register your models here.


admin.site.register(Movie, MovieAdmin)

# ? sonrasında py manage.py makemigrations komutu ile modelimizde yaptığımız değişiklikleri algılayarak bir migration dosyası oluşturuyoruz. Bu dosya, veritabanında yapılacak değişiklikleri tanımlar. Eğer modelinizde yeni bir alan eklediyseniz veya mevcut bir alanı değiştirdiyseniz, bu komutu çalıştırarak Django'ya bu değişiklikleri bildirebilirsiniz.