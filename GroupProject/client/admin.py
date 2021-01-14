from django.contrib import admin

# Register your models here.
from .models import User, Klient, KlientManager, Pracownik, \
    PracownikManager, Kierownik, KierownikManager,  Warsztat, WarsztatManager

admin.site.register(User)
admin.site.register(Klient)
# admin.site.register(KlientManager)
# admin.site.register(KlientMore)
admin.site.register(Pracownik)
# admin.site.register(PracownikManager)
# admin.site.register(PracownikMore)
admin.site.register(Kierownik)
# admin.site.register(KierownikManager)
# admin.site.register(KierownikMore)
admin.site.register(Warsztat)
# admin.site.register(WarsztatManager)
# admin.site.register(WarsztatMore)

