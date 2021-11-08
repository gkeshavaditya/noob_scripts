# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Keshavaditya Golla"
__email__ = "keshav.aditya19@gmail.com"


def total_hotel_cost(nights):
    hotel_cost_per_day = 140
    return hotel_cost_per_day * nights


def plane_ride_cost(city):
    plane_cost = {
        "charlotte":    183,
        "tampa":        220,
        "pittsburgh":   222,
        "los angeles":  475
    }
    return plane_cost[city.lower()]


def rental_car_cost(days):
    total_cost = 0
    rental_car_cost_per_day = 40
    if days >= 7:
        total_cost = (rental_car_cost_per_day * days) - 50
    elif days >= 3:
        total_cost = (rental_car_cost_per_day * days) - 20
    elif days < 3:
        total_cost = rental_car_cost_per_day * days

    return total_cost


def trip_cost(city, days, spending_money):
    total = rental_car_cost(days) + plane_ride_cost(city) + total_hotel_cost(days - 1) + spending_money
    return total


print('Please enter a city from the following:\n '
      'Charlotte \n '
      'Tampa\n '
      'Pittsburgh\n '
      'Los Angeles')
city = input('->')
days = int(input('The no. of days \n-'))
money = float(input('Enter you budget\n-'))
print(trip_cost(city, days, money))
