from flask_restful import abort

from products import Product
from flask import Flask, jsonify, request

app = Flask(__name__)
products = Product()

USD_TO_EGP = 15.71


# Subtotal
def calculate_total_price(items, currency):
    totalPrice = 0
    productItems = products.get_product()

    for item in items:
        exist = False  # check product is in list
        for productItem in productItems:
            if item == productItem["name"]:
                exist = True
                totalPrice += productItem["price"]
                break
        if not exist:
            abort(400)
    if currency == "EGP":
        totalPrice *= USD_TO_EGP

    return totalPrice


# Taxes
def calculate_taxes(total_price):
    taxes = total_price * 0.14
    return taxes


# Discounts
def calculate_discount(items, currency):
    discountDescription = []
    totalDiscount = 0
    itemDiscount = 0
    numbersOfShirts = 0
    numberOfJackets = 0
    productItems = products.get_product()
    factor = 1
    if currency == "EGP":
        currency = "e£"
        factor = USD_TO_EGP
    elif currency == "USD":
        currency = "$"

    for item in items:
        if item == "Shoes":
            for productItem in productItems:
                if item == productItem["name"]:
                    itemDiscount = productItem["price"] * 0.1 * factor
                    totalDiscount += itemDiscount
                    break
            discountDescription.append("10% off shoes: -" + currency + str(round(itemDiscount, 4)))

        if item == "T-shirt":
            numbersOfShirts += 1
        if item == "Jacket":
            numberOfJackets += 1
    if numbersOfShirts > 1 and numberOfJackets > 0:
        if numberOfJackets > int(numbersOfShirts / 2):
            numberOfJackets = int(numbersOfShirts / 2)

        for productItem in productItems:
            if productItem["name"] == "Jacket":
                itemDiscount = productItem["price"] * 0.5 * factor
                totalDiscount += itemDiscount * numberOfJackets
                break
        for i in range(numberOfJackets):
            discountDescription.append("50% off jacket: -" + currency + str(round(itemDiscount, 4)))

    discount = {'discountDescription': discountDescription, 'totalDiscount': totalDiscount}

    return discount


# Format discount
def format_discount(discount):
    discountDescription = ""
    for i in range(len(discount['discountDescription'])):
        discountDescription += '\n\t\t' + discount['discountDescription'][i]
    return discountDescription


# get products
@app.route('/products')
def get_products():
    product = products.get_product()
    if not product:
        abort(404)
    return jsonify({
        'products': products.get_product()
    })


# get offers
@app.route('/offers')
def get_offers():
    return jsonify({
        'offers': products.get_offers()
    })


# calculate cart
@app.route('/price/<currency>')
def get_total_price(currency):
    items = request.get_json()

    if not items["cart"]:
        abort(400)
    totalPrice = calculate_total_price(items["cart"], currency)
    taxes = calculate_taxes(totalPrice)
    discount = calculate_discount(items["cart"], currency)
    total = round(totalPrice + taxes - float(discount["totalDiscount"]), 4)
    if currency == "EGP":
        currency = "e£"
    elif currency == "USD":
        currency = "$"
    else:
        abort(422)
    try:
        if discount["totalDiscount"] == 0:
            return str(
                f"Sub total : {currency + str(round(totalPrice, 4))}\n"
                f"Taxes : {currency + str(round(taxes, 4))}\n"
                f"Total : {currency + str(round(total, 4))} "
            ), 200
        else:
            return str(
                f"Sub total: {currency + str(round(totalPrice, 4))}\n"
                f"Taxes: {currency + str(round(taxes, 4))}\n"
                f"Discounts: {str(format_discount(discount))}\n"
                f"Total: {currency + str(round(total, 4))}"
            ), 200
    except:
        abort(500)


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def not_processable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "not processable"
    }), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(500)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500
