from django.contrib import admin
from .models import Customer, Domain, Score, Role, Study, Message, Study_Message

# Register your models here.
admin.site.register(Customer)
admin.site.register(Domain)
admin.site.register(Score)
admin.site.register(Role)
admin.site.register(Study)
admin.site.register(Message)
admin.site.register(Study_Message)