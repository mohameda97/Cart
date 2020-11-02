# Edfa3ly/Yashry Backend
Write a program that can price a cart of products, accept multiple products, combine offers, and display a total detailed bill in different currencies (based on user selection).
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.


## Running the server

From within the `Cart` directory.

To run the server on Widows , execute:

```bash
set FLASK_APP=flaskr
flask run --reload
```
To run the server on Linux , execute:

```bash
export FLASK_APP=flaskr
flask run --reload
```



## Testing
To run the tests, run
```
python test_cases.py
```
## API Documentation 


## Getting Started

* Base URL: The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.


# Error Handling
Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
```
The API will return three error types when requests fail:

* 400: Bad Request
* 404: Resource Not Found
* 422: Not Processable
* 500: Internal Server Error
# Endpoints

#### GET/products
###### General 
return a list from all products
###### Sample
from postman write http://127.0.0.1:5000/products and select GET method
```
{
  "products":[
              {
                "name":"T-shirt",
                "price":10.99
              },
              {
                "name":"Pants",
                "price":14.99
              },
              {
                "name":"Jacket",
                "price":19.99
              },
              {
                "name":"Shoes",
                "price":24.99
              }
             ]
}

```
#### GET/offers
###### General 
return a list from all offers
###### Sample
from postman write http://127.0.0.1:5000/offers and select GET method
```
{
 "offers":[
           {"1":"Buy two t-shirts and get a jacket half its price"},
           {"2":"Shoes are on 10% off"}
          ]
}

```
#### GET/price/USD
###### General 
calculate total price of cart in USD
###### Sample
from postman write http://127.0.0.1:5000/price/USD and select GET method 
###### Request Body
Insert this form in postman body
```
    {
    "cart":["T-shirt","T-shirt","Jacket","Shoes"]
    }
```
###### Request Response

```           
Sub total: $66.96
Taxes: $9.3744
Discounts: 
	10% off shoes: -$2.499
	50% off jacket: -$9.995
Total: $63.8404
```
#### GET/price/EGP
###### General 
calculate total price of cart in EGP
###### Sample
from postman write http://127.0.0.1:5000/price/EGP and select GET method 
###### Request Body
Insert this form in postman body
```
    {
    "cart":["T-shirt","Pants"]
    }
```
###### Request Response

```           
Sub total : e£408.1458
Taxes : e£57.1404
Total : e£465.2862 
```

