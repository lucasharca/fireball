from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.domain.exceptions import InvalidRollParametersError
from api.routes import dice
from api.schemas.response.error_response import ErrorResponse

app = FastAPI(title="Fireball")


@app.exception_handler(InvalidRollParametersError)
async def invalid_roll_parameters_handler(
    request: Request, exc: InvalidRollParametersError
) -> JSONResponse:
    error = ErrorResponse(
        code="INVALID_ROLL_PARAMS",
        message=str(exc),
        details=exc.details or None,
    )
    return JSONResponse(status_code=400, content=error.model_dump())


@app.exception_handler(Exception)
async def unhandled_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    error = ErrorResponse(
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected error occurred.",
    )
    return JSONResponse(status_code=500, content=error.model_dump())


app.include_router(dice.router, prefix="/dice", tags=["Dice"])