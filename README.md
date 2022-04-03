# nBuysell
A Marketplace for buy sell new and old products!


# Live link: <a href="https://nbuysell.pythonanywhere.com/">nBuySell</a>
If you'd like to check as a user. Here is credential:

User: john
<br>password: password4john

## Setup
#### The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Bappy4u/storefront.git
$ cd nBuySell
```

#### Create a virtual environment to install dependencies in and activate it:
if you have `pipenv`  installed in your machine
```sh
$ pipenv install
```
It will install a virtual environment for you and will install all the dependencies
* Select that environment as your python interpreter

Once you select and run virtual environment that you just installed :

* To migrate all the settings command this in the terminal
```sh
(nBuySell) $ python manage.py migrate
```
* Finally 

```sh
(storefront) $ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/


* To check the admin pannel create a super user

```sh
(nBuySell) $ python manage.py createsuperuser
```


# What I've used in this project

#### * Python 3.8
#### * Django
#### * Django-orm
#### * JavaScript
#### * SQLite
#### * pythonanywhere.com for deployment


# Incomplete feature:

#### * Live chat person to person


<h2>Walkthrough</h2>

### Homepage
![home](https://user-images.githubusercontent.com/26277680/149951308-372580b6-5767-4f51-a1ce-7e941d51b251.png)


### Product Page
![prod-cat](https://user-images.githubusercontent.com/26277680/149951367-a1e5655a-04be-41b7-bca5-39158640fba1.png)


### My product Page

![my-product-cat](https://user-images.githubusercontent.com/26277680/149958661-4490c255-a2ed-4b76-bf95-89503a77f384.png)



### Add product

![add-product-form](https://user-images.githubusercontent.com/26277680/149958236-7d498bea-03cb-4e87-8a63-a9ffa50e543f.png)



### Drag and drop image upload page

![image upload](https://user-images.githubusercontent.com/26277680/149958338-25f25d02-ff36-41a9-a615-8b55981700b9.png)


### Product Edit page
![edit-prod](https://user-images.githubusercontent.com/26277680/149958075-7104693b-19ae-4b34-96e0-2d0bcb3e9090.png)


### My product & Saved product listing page
![saved-product](https://user-images.githubusercontent.com/26277680/149958808-c589a36a-e0b6-41e7-b965-5b8ded4cc194.png)



### Login
![login](https://user-images.githubusercontent.com/26277680/149951397-6f5e4701-0288-4251-a434-010a4033a097.png)

### Signup Page
![sign-up](https://user-images.githubusercontent.com/26277680/149951469-008be4bb-d1c6-4eb1-ad88-32c189d665bb.png)
