from django.shortcuts import render
from .forms import RegisterComedianForm
from .models import RegisterComedian
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail


# Create your views here.

def register_comedians(request):
    if request.method == 'POST':
        form = RegisterComedianForm(request.POST)
        if form.is_valid():
            r = form.save()

            r_details = r.__dict__

            email_from = settings.EMAIL_HOST_USER
            email_to = r.email
            email_admin = settings.EMAIL_ADMIN

            content = {"%s: %s" % (key,value) for (key, value) in r_details.items()}
            content = "\n".join(content)

            message1 = ('Thank you for your interest!', 'We will get back to you.', email_from, [email_to])
            message2 = ('New comedian registration', content , email_from, [email_admin])
            send_mass_mail((message1, message2), fail_silently=False)

        return render(request, 'comedians/thankyou.html', {'r': r})

    else:
        form = RegisterComedianForm()

    return render(request, 'comedians/register_comedians.html', {'form': form})


def view_comedians(request):
    AllComedians = RegisterComedian()
    all_com = AllComedians.get_all_objects()
    return render(request, 'comedians/view_comedians.html',{'all_com': all_com})
