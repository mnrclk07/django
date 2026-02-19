from django.contrib import admin
from .models import Movie

# Register your models here.


admin.site.register(Movie)

# ? sonrasında py manage.py makemigrations komutu ile modelimizde yaptığımız değişiklikleri algılayarak bir migration dosyası oluşturuyoruz. Bu dosya, veritabanında yapılacak değişiklikleri tanımlar. Eğer modelinizde yeni bir alan eklediyseniz veya mevcut bir alanı değiştirdiyseniz, bu komutu çalıştırarak Django'ya bu değişiklikleri bildirebilirsiniz.