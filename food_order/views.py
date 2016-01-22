from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, Http404
from .models import Food, User, Order
from django.db import IntegrityError

def index(request):
    food_list = Food.objects.order_by('name')
    # template = loader.get_template('order/index.html')
    context = {
        'food_list': food_list,
    }

    return render(request, 'order/index.html', context)

    # return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the food_order index.")


def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    try:
        food = Food.objects.get(pk=food_id)
        users = food.users.all()

    except Food.DoesNotExist:
        raise Http404("Food does not exist")

    return render(request, 'order/detail.html', {'food': food, 'users_list': users})
    # return HttpResponse("Ban dang xem danh sach user dat mon: %s." % food_id)

def detail2(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    users = food.users.all()
    return render(request, 'order/detail.html', {'food': food, 'users_list': users})


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    food = Food.objects.order_by('name')
    try:
        select_food = Food.objects.get(pk=request.POST['food'])
    except(KeyError, Food.DoesNotExist):
        return render(request, 'order/order.html', {
            'user': user,
            'food_list': food,
            'error_message': "You didn't select a food.",
        })
    else:
        try:
            order = Order(user_id, select_food.id)
            order.save()
        except IntegrityError as e:
            return render(request, 'order/order.html', {
                'user': user,
                'food_list': food,
                'error_message': "Duplication",
            })
        return HttpResponse("Ban dang xem danh sach user dat mon: %s." % user_id)