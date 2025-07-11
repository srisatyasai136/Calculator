from django.shortcuts import render

def calculator(request):
    result = ''
    expression = ''

    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = eval(expression)
        except:
            result = 'Error'

    return render(request, 'calculator.html', {'expression': expression, 'result': result})