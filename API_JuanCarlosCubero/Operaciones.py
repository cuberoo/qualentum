from fastapi import FastAPI 
from datetime import datetime

app = FastAPI()

@app.get("/sumar/{num1}/{num2}")
def dividir(num1: int, num2: int):
    num1 = num1,
    num2 = num2
    return{
        num1+num2
    }

@app.get("/restar/{num1}/{num2}")
def dividir(num1: int, num2: int):
    num1 = num1,
    num2 = num2
    return{
        num1-num2
    }

@app.get("/multiplicar/{num1}/{num2}")
def dividir(num1: int, num2: int):
    num1 = num1,
    num2 = num2
    return{
        num1*num2
    }
    
@app.get("/dividir/{dividendo}/{divisor}")
def dividir(dividento: int, divisor: int):
    Ndividento = dividento,
    Ndivisor = divisor
    return{
        Ndividento/Ndivisor
    }