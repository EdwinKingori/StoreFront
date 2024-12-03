from django.shortcuts import render
from django.db.models import Q, Func, F, Value
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from shop.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem
# Create your views here.


def index(request):
    # selecting fields to query
    # product = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # using select_related (1 instance) and prefetch_related (n objects)
    # product = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()

    # # exercise: get the last 5 orders with their customers and items (include product)
    # orders = Order.objects.select_related(
    #     'customer').order_by('-placed_at')[:5].prefetch_related('orderitem_set__product').all()

    # Annotating and calling database functions
    new_column = Customer.objects.annotate(
        full_name=Func(F('first_name'), Value(
            ' '), F('last_name'), function='CONCAT')
    )

    # a shorterannotating code for the above
    queryset = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )

    context = {
        # 'products': product,
        'queryset': queryset,
        'new_column': new_column,
    }
    return render(request, 'playground/index.html', context)
