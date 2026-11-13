from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(
    title="Arithmetic Service",
    version="0.1.0",
    description="A simple FastAPI service for basic arithmetic operations.",
)


class ArithmeticRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    a: int | float = Field(..., description="First number", examples=[10])
    b: int | float = Field(..., description="Second number", examples=[3])


class ArithmeticResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    a: int | float = Field(..., description="First number")
    b: int | float = Field(..., description="Second number")
    result: int | float = Field(..., description="Arithmetic result")


@app.get("/", summary="Health check")
def read_root() -> dict[str, str]:
    return {"message": "Arithmetic API is running"}


@app.post("/add", response_model=ArithmeticResponse, summary="Add two numbers")
def add_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a + payload.b)


@app.post(
    "/subtract", response_model=ArithmeticResponse, summary="Subtract two numbers"
)
def subtract_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a - payload.b)


@app.post(
    "/multiply", response_model=ArithmeticResponse, summary="Multiply two numbers"
)
def multiply_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a * payload.b)


@app.post("/divide", response_model=ArithmeticResponse, summary="Divide two numbers")
def divide_numbers(payload: ArithmeticRequest) -> ArithmeticResponse:
    if payload.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")

    return ArithmeticResponse(a=payload.a, b=payload.b, result=payload.a / payload.b)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
