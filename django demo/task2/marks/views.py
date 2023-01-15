from django.shortcuts import render


def main(request):
    return render(request, 'home.html')


def result(request):
    if request.method == 'GET':
        n = request.GET['t1']
        r = request.GET['t2']
        p = int(request.GET['t3'])
        c = int(request.GET['t4'])
        b = int(request.GET['t5'])
        tm = p + c + b
        if tm >= 250:
            g = 'A'
        elif tm >= 200:
            g = 'B'
        elif tm >= 150:
            g = 'C'
        else:
            g = 'Fail'
        return render(request, 'result.html', {'nm': n, 'roll': r, 'pm': p, 'cm': c, 'bm': b, 'tm': tm, 'g': g})
