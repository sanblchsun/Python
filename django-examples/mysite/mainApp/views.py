from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contacts(request):
    return render(request, 'mainApp/contacts_html.html', {
        'values':
            [
                'Позвоните в отдел кадров по телефону: ',
                '+7(111)-111-11-11',
                'или пишите на почту: ',
                'info@info.ru'
            ]})
