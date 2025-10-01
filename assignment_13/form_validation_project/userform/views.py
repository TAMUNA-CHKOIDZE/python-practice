from django.contrib import messages
from django.shortcuts import render, redirect

from userform.forms import UserSubmissionForm


def submit_view(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            instance = form.save()  # ← ვინახავ ფორმის ობიექტს instance ცვლადში
            username = instance.username  # ← ვიღებ იუზერის სახელს და ვინახავ username
            return redirect(f'/submit_page/?username={username}') # სახელის გადაცემა context-ით, redirect-ის დროს URL-თან ერთად username query param-ით
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSubmissionForm()

    return render(request, template_name='form.html', context={'form': form})


# submit_page-მა უნდა მიიღოს username URL-დან (query param-იდან)
def submit_page(request):
    username = request.GET.get('username', 'User')  # მომაწოდე URL-დან 'username'-ის მნიშვნელობა, და თუ არ არის, მაშინ გადმომეცი ტექსტი 'User' როგორც ნაგულისხმევი (default) მნიშვნელობა.
    return render(request, 'submit.html', {'username': username})
