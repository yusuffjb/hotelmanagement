from fastapi import Request
# from scripts.core.db.mongo_db import collection, deluxe_databases, suite_databases
from schemas.models import customers, Booking
from scripts.logging.log_config import logging
from fastapi.templating import Jinja2Templates
from scripts.core.db.mongo_utility import mongo

templates = Jinja2Templates(directory="templates")


async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


async def delete(request: Request):
    return templates.TemplateResponse("delete.html", {"request": request})


async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


async def signup_standardroom(request: Request):
    return templates.TemplateResponse("standardroom.html", {"request": request})


async def Deluxe(request: Request):
    return templates.TemplateResponse("Deluxeroom.html", {"request": request})


async def Suite(request: Request):
    return templates.TemplateResponse("Suite.html", {"request": request})


async def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})


async def find_all_customers_details(request: Request):
    data = await request.form()
    logging.debug('signup')
    temp = customers(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    insert = mongo.for_insert_one("Yusuff_INT_767",temp)
    if insert:
        return {"message": "Data found Successfully"}
    else:
        return {"error": "data not fount"}


async def customers_signup(request: Request):
    data = await request.form()
    logging.debug('signup')
    temp = customers(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    result = mongo.for_insert_one("Yusuff_INT_767",temp)
    return {"message": "Sign up page created successfully"}


async def customers_signup1(request: Request):
    data = await request.form()
    logging.debug('standard')
    temp = Booking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("Yusuff_INT_767",temp)
    if result:
        return {"message": "Standard booked successfully"}
    else:
        retrun



async def customers_signup2(request: Request):
    data = await request.form()
    logging.debug('deluxe')
    temp = Booking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("yusuff_1",temp)
    return {"message": "deluxe booked successfully"}


async def customers_signup_suite(request: Request):
    data = await request.form()
    logging.debug('suite')
    temp = Booking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("yusuff_2",temp)
    if result:
        return {"message": "suite booked successfully"}
    else:
        return{"not booked"}


async def customers_login(request: Request):
    data = await request.form()
    logging.debug('login')
    username = data["username"]
    password = data["password"]
    find = {"username": username, "password": password}
    temp = mongo.for_find_one("Yusuff_INT_767",find)
    if temp:
        return templates.TemplateResponse("welcome.html", {"request": request})
    else:
        return {"error": "Login failed,username or password is wrong!!"}


async def customers_delete(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"]
    find = {"username": username, "password": password}
    temp = mongo.for_find_one("Yusuff_INT_767",find)
    # print(temp)
    if temp:
        delete = {"username": username }
        mongo.for_delete_one("Yusuff_INT_767",delete)
        return {"message: successfully deleted "}
    else:
        return {"message: not deleted"}
