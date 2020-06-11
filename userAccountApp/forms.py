from django import forms
from userAccountApp.models import Payout, User
from django.core import validators


class PayoutForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.HiddenInput)

    amount = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ), validators=[validators.MinValueValidator(0)])

    account = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Payout
        fields = ('user', 'amount', 'account')

    def clean_amount(self):
        userId = int(self.data['user'])
        user = User.objects.get(pk=userId)
        amount = float(self.data['amount'])
        if user.totalReward < amount:
            raise forms.ValidationError('User have not enough money!')
        return float(self.data['amount'])
