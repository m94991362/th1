# Create your views here.
from datetime import datetime
from json import JSONEncoder

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from web.models import User, Expense,Income,Token


@csrf_exempt
def submit_expense(request):
    # TODO:
    # 1)validate Data
    # 2)user might be fake
    # 3)token might be fake
    this_token = request.POST['token']

    if 'date' in request.POST:
        date = request.POST['date']
    if 'date' not in request.POST:
        date = datetime.now()
    this_user = User.objects.filter(token__token=this_token).get()
    newExpense = Expense.objects.create(
        user=this_user,
        amount=request.POST['amount'],
        text=request.POST['text'],
        date=date
    )

    return JsonResponse({
        'status': 'OK',
        'data': {
            'name': newExpense.text,
            'amount': newExpense.amount
        }
    }, encoder=JSONEncoder)
@csrf_exempt
def submit_income(request):
    # TODO:
    # 1)validate Data
    # 2)user might be fake
    # 3)token might be fake
    this_token = request.POST['token']

    if 'date' in request.POST:
        date = request.POST['date']
    if 'date' not in request.POST:
        date = datetime.now()
    this_user = User.objects.filter(token__token=this_token).get()
    newIncome = Income.objects.create(
        user=this_user,
        amount=request.POST['amount'],
        text=request.POST['text'],
        date=date
    )

    return JsonResponse({
        'status': 'OK',
        'data': {
            'name': newIncome.text,
            'amount': newIncome.amount
        }
    }, encoder=JSONEncoder)
