def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return int(denomination * number_of_bills)


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    #bills = get_number_of_bills(budget, denomination)
    
    #bulls = exchange_rate + (spread / 100)
    #bills = budget / (exchange_rate + (spread / 100)) # AssertionError: 9337.068160597573 != 8568
    
    #return ((budget / (exchange_rate+(spread/100))) // denomination) * denomination
    #return (int((budget / denomination) * (exchange_rate+(spread/100))) // denomination)
    #return (127.25 / (1.2+(10/100))) // 20 * 20 #pedig ez 80 mint a példában
    #return (127.25 / (1.2+(10/100))) // 5 * 5 #pedig ez 95 mint a példában
    #return (100000 / (10.61+(10/100))) // 1 * 1 #de ez nem 8568 mint a példában hanem 9337
    #return (budget / denomination) // (exchange_rate+(100/spread))
    #return bills // bulls # 9337 megint
    #return int((budget // (exchange_rate+(exchange_rate*(spread/100))))) # nem jöttem rá mit kellene csinálni a denominationnel mit kell osztani szorozni mivel

    #return 100000 // (10.61*1.1)
    return (((budget // (exchange_rate*(1+(spread/100)))) // denomination) * denomination)