from django.shortcuts import render

# Create your views here.


def enter(request):
    return render(request, 'enter_num.html')


def result(request):
    if request.method == 'POST':
        data = request.POST
        context = {
            'first': int(data.get('first')),
            'second': int(data.get('second')),
            'operation': data.get('operation')
        }
        if context['operation'] == 'add':
            result = context['first'] + context['second']
            context['result'] = result
            context['operation'] = '+'
            return render(request, 'result.html', context)
        elif context['operation'] == 'subtract':
            result = context['first'] - context['second']
            context['result'] = result
            context['operation'] = '-'
            return render(request, 'result.html', context)
        elif context['operation'] == 'multiply':
            result = context['first'] * context['second']
            context['result'] = result
            context['operation'] = '*'
            return render(request, 'result.html', context)
        elif context['operation'] == 'divide':
            if context['second'] != 0:
                if not context['first'] % context['second']:
                    result = context['first'] / context['second']
                    context['result'] = f'{result:.0f}'
                    context['operation'] = '/'
                    return render(request, 'result.html', context)
                else:
                    result = context['first'] / context['second']
                    context['result'] = f'{result}'
                    context['operation'] = '/'
                    return render(request, 'result.html', context)
            else:
                return render(request, 'divide_error.html', context)





