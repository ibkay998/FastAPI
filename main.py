from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://cors-test.codehappy.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Msg(BaseModel):
    msg: str


class Operations(str, Enum):
    multiplication = "multiplication"
    addition = "addition"
    subtraction = "subtraction"


class ShemaResponse(BaseModel):
    operation_type:Operations
    x:int
    y:int


@app.get("/")
async def root(response: Response):
    response.headers["access-control-allow-origin"] = "*"
    return {
        "slackUsername": "ibkay998",
        "backend":True,
        "age":23,
        "bio":"Hi my name is ibukunoluwa oyeniyi and an aspiring software developer interested both in frontend and backend and I love solving problems"
    }


@app.post("/post",status_code=201)
async def calculate(response: ShemaResponse):
    x = response.x 
    y = response.y
    if response.operation_type == Operations.addition:
        ans = x + y
    elif response.operation_type == Operations.subtraction:
        ans = x - y
    else:
        ans = x*y
    return {"slackUsername":"@ibkay998", "result": ans, "operation_type": response.operation_type}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
