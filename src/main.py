from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Add Service",
    version="0.1.0",
    description="A simple FastAPI demo service for adding two numbers.",
)


class ArithmeticRequest(BaseModel):
    a: int | float = Field(..., description="First number")
    b: int | float = Field(..., description="Second number")


class ArithmeticResponse(BaseModel):
    a: int | float = Field(..., description="First number")
    b: int | float = Field(..., description="Second number")
    result: int | float = Field(..., description="Arithmetic result")


@app.get("/", summary="Health check")
def read_root() -> dict[str, str]:
    return {"message": "Add API is running"}


@app.post("/add", response_model=ArithmeticResponse, summary="Add two numbers")
def add_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a + payload.b)


@app.post(
    "/subtract", response_model=ArithmeticResponse, summary="Subtract two numbers"
)
def subtract_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a - payload.b)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
