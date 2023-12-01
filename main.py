from typing import Union
import st_con
from fastapi import FastAPI, Request, Body
from fastapi.responses import RedirectResponse
import time
import requests
import json

app = FastAPI()

def btn(state):
     print("Кнопку нажали!", state)

clientId = "PROJECT CLIENT ID"
clientSecret = "PROJECT CLIENT SECRET"
deviceProfileID = "Device Profile ID"

st = st_con.SmartThingsCon(btn, clientId, clientSecret, deviceProfileID)

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/<username>/test_btn")
async def ffff(state):
      st.send_btn(state)

@app.post("/<username>")
async def show_body(data = Body()):
    body_content = data
    type, tt = st.read_response(data)

    return tt