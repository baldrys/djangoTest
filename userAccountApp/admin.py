from django.contrib import admin
from userAccountApp.models import *
from django.conf.urls import url
from django.http import HttpResponseRedirect
from datetime import datetime
import requests

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'totalReward')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('author', 'amount', 'date')


class PayoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'account', 'dateProcess', 'status')
    change_form_template = 'admin/payouts/payouts_change_form.html'
    fields = (
        'user',
        'amount',
        'status',
        'account'
    )

    def get_readonly_fields(self, request, obj=None):
        if obj.status == True:  # editing an existing object
            return self.readonly_fields + ('user', 'amount', 'account')
        return self.readonly_fields

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url('^(?P<id>\d+)/process-payout/$',
                self.processPayout, name='process-payout')
        ]
        return custom_urls + urls

    def processPayout(self, request, id):
        payout = Payout.objects.get(id=id)
        payout.dateProcess = datetime.now()
        payout.status = True
        payout.save()
        user = User.objects.get(payout__id=id)
        user.totalReward -= payout.amount
        user.save()
        post_data = {
            'account': payout.account,
            'amount': payout.amount
        }
        response = requests.post(
            'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4', data=post_data)
        content = response.content
        print("content", content)
        return HttpResponseRedirect("../")


admin.site.register(Payout, PayoutAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(User, UserAdmin)
