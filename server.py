from fastapi import FastAPI

# FastAPI Test
app = FastAPI()

# Route
@app.get('/')
async def root():
    return "Hello, World"

