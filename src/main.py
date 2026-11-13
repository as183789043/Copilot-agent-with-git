from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Add Service",
    version="0.1.0",
    description="A simple FastAPI demo service for adding two numbers.",
)


class AddRequest(BaseModel):
    a: float = Field(..., description="First number to add")
    b: float = Field(..., description="Second number to add")


class AddResponse(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")
    result: float = Field(..., description="Sum of the two numbers")


@app.get("/", summary="Health check")
def read_root() -> dict[str, str]:
    return {"message": "Add API is running"}


@app.post("/add", response_model=AddResponse, summary="Add two numbers")
def add_numbers(payload: AddRequest) -> AddResponse:
    return AddResponse(a=payload.a, b=payload.b, result=payload.a + payload.b)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
