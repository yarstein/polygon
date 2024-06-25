import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import get_balance, get_balance_batch, get_token_info


def get_balance_view(request):
    """
    Представление, для получения баланса адреса
    """
    address = request.GET.get('address')
    balance = get_balance(address)
    return JsonResponse({"balance": balance})


@csrf_exempt    # разрешаем без проверки CSRF т.к. в postmap ловил ошибку csrf
def get_balance_batch_veiw(request):
    """
    Представление,для обработки GET или POST запросов нескольких адресов сразу
    """
    if request.method == 'POST':
        body = json.loads(request.body)
        addresses = body.get('addresses', [])
        balances = get_balance_batch(addresses)
        return JsonResponse({"balances": balances})
    else:
        addresses = request.GET.get('addresses')
        # вот тут решение искал долго незнал, что это строка содержащий json,
        # используем json.loads - чтобы преобразовать строку json в список python
        addresses = json.loads(addresses)
        balances = get_balance_batch(addresses)
        return JsonResponse({"balances": balances})
    

def get_token_info_view(request):
    """
    Представление, для получения информаций адреса
    """
    address = request.GET.get('address')
    info = get_token_info(address)
    return JsonResponse(info)