from typing import Callable

from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Manufacturer, Car, Driver


def index(request: HttpRequest) -> Callable:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)
