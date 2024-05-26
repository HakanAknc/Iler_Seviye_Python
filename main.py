from fastapi import FastAPI              # uvicorn main:app --reload  

app = FastAPI()

@app.get("/")
async def get():     
    return {"message": "Hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.delete("/")
async def delete():
    return {"message": "hello from the put route"}


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def get():
#     return {"message": "Hello worlddsfddddddd"}

# if __name__ == "__main__":
#     app.run(debug=True)


