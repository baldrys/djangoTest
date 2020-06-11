from django.shortcuts import render, get_object_or_404
from userAccountApp.models import User
from userAccountApp.forms import PayoutForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})


def user(request, id):
    user = get_object_or_404(User, id=id)
    form = PayoutForm(request.POST or None, initial={
        'user': user
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('user', kwargs={'id': id})))
    return render(request, 'users/user.html', {
        'user': user,
        'form': form,
        'sent': request.GET.get('sent', False)
    })
