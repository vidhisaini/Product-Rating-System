# Product-Rating-System
This is a submission for the assignment by CasaOne for the Position of Software Developer.

The following assignment provides insights about the design flow, architectural diagram and APIs to rate products purchased by a customer, also fetch average individual ratings.

## Assumptions

- Product Table exists where all the products are listed with their *product_id*, *total-ratings* & *average_ratings*
- Any new product in the catalogue has also been inserted in tha table with *total-ratings = 0* & *average_ratings = 0*

## Pre-requisites 
- Python 3.6 and pip should be preinstalled

## How to Run it Locally

- Clone Repository
- Install the requirements using `pip install -r requirements.txt`, in the repository folder.
- Run `python app.py`

## Technology Stack

- Programming Languages
    - Python 3.6
    
- Frameworks
  - Flask 2.0.1

- Database
     - SQLAlchemy 1.4.17

- APIs
    - REST Api
    
## Database Schema
```
class Product(db.Model):
    product_id = db.Column(db.String(32), primary_key=True)
    total_ratings = db.Column(db.Integer)
    average_ratings = db.Column(db.Integer)

    def __init__(self,product_id, total_ratings, average_ratings):
        self.product_id = product_id
        self.total_ratings = total_ratings
        self.average_ratings = average_ratings
```
    
## Workflow
<img src="https://imgur.com/qqk9a4J.png" width="65%"/>

## Formats for APIs

- **GET API** (Fetch product ratings)
 
  - Fetch Particular Product
      - Request URL (http://127.0.0.1:5000/fetch-products?product_id=4) for particular product with product_id = 4
      - Response -
```
    {
    "average_ratings": 3,
    "product_id": "4",
    "total_ratings": 6
    }
```                  
                  
<img src="https://imgur.com/t6oivS6.png" width="50%"/>

- Fetch all the products
      - Request URL (http://127.0.0.1:5000/fetch-products) for all the products in the database
      - Response -
      
                [
                  {
                      "average_ratings": 2.8,
                      "product_id": "4",
                      "total_ratings": 5
                  },
                  {
                      "average_ratings": 4.6,
                      "product_id": "5",
                      "total_ratings": 5
                  }
                ]
                
      - <img src="https://imgur.com/6hFqSdp.png" width="50%"/>
      
- **PUT API** (Rate Product)

  - Request URL (http://127.0.0.1:5000/rate-product)
      - Body - List of JSON Objects 
      
            [
                {
                  "product_id": "9",
                  "rating": 4
                },
                {
                  "product_id" : "4",
                  "rating" : 4
                }
             ]
              
     - Response - 
      
                [
                    {
                        "Message": "Product with product id 9 does not exist!"
                    },
                    {
                        "Message": "Rating of product with product id 4 has been saved successfully!"
                    }
                ]
     - <img src="https://imgur.com/ELw0yxU.png" width="50%"/>
     
- **POST API**
  
  - Request URL - (http://127.0.0.1:5000/add-product)
  - Body - 
  
        [
            {
              "product_id" : "7",
              "total_ratings" : 4,
              "average_ratings" : 2
            },
            {
              "product_id" : "8",
              "total_ratings" : 4,
              "average_ratings" : 2
            }
         ]
    - Response - 
              
              [
              {"Message": "Product with product id 7 inserted!"},
              {"Message": "Product with product id 8 inserted!"}
              ]
    - <img src="https://imgur.com/mBmuq4M.png" width="50%"/>
  

## Note
- POST API is used for testing purposes
- All the APIs are tested using Postman
- This assignment deals with APIs for fetching and rating products, Event Scheduler is theoretical part here.
- Further modifications can be done by integrating *review description* of each product, optional though.
