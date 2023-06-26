from fastapi import Request, APIRouter
from fastapi import FastAPI, Request
from scripts.core.handlers import room_handler
from scripts.constants.app_constants import fastrun

app_router = APIRouter()


@app_router.get(fastrun.customersignup)
async def function(request: Request):
    try:
        return await room_handler.signup(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.get(fastrun.customerdelete)
async def function(request: Request):
    try:
        return await room_handler.delete(request)
    except Exception as e:
        return {"error",str(e)}



@app_router.get("/")
async def function(request: Request):
    try:
        return await room_handler.login(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.get(fastrun.standardroom)
async def function(request: Request):
    try:
        return await room_handler.signup_standardroom(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.get(fastrun.deluxeroom)
async def function(request: Request):
    try:
        return await room_handler.Deluxe(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.get(fastrun.suite)
async def function(request: Request):
    try:
        return await room_handler.Suite(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.get(fastrun.booking)
async def function(request: Request):
    try:
        return await room_handler.welcome(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.customerdetail)
async def function(request: Request):
    try:
        return await room_handler.find_all_customers_details(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.customersignup)
async def function(request: Request):
    try:
        return await room_handler.customers_signup(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.standardbooking)
async def function(request: Request):
    try:
         return await room_handler.customers_signup1(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.deluxebooking)
async def function(request: Request):
    try:
         return await room_handler.customers_signup2(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.suitebooking)
async def function(request: Request):
    try:
         return await room_handler.customers_signup_suite(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.customerlogin)
async def function(request: Request):
    try:
        return await room_handler.customers_login(request)
    except Exception as e:
        return {"error",str(e)}


@app_router.post(fastrun.customerdelete)
async def function(request: Request):
    try:
         return await room_handler.customers_delete(request)
    except Exception as e:
        return {"error",str(e)}
