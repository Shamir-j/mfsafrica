Closet Pair Point API using Divide and Conquer Algorithm

## Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`

# To access the application in production

8. https://shamirmfsafrica.herokuapp.com/login to access the simple application UI. Note the Login button is not working

9. To test the API in production head to this endpints

10. https://shamirmfsafrica.herokuapp.com/api-auth/points/ post the data in a json format to get the return of the closetpoint pair and the input points strimngs pair and the smallest distance.

    {
        "points": "(3,5), (2,3), (4,5), (7,6), (4,5), (8,4), (6,7), (9,8)"
    },
11. to get all points and theoir closet point pair perform a get request on the above endpoint

12. To perform delete, get a single object, or update of the points use the following uirl
    https://shamirmfsafrica.herokuapp.com/api-auth/pointdetail/<int:pk>  the int: pk argument takes the primary key of the record iun the database i.e see below
    https://shamirmfsafrica.herokuapp.com/api-auth/pointdetail/3/

13. Enjoy
