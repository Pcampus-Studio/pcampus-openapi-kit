from __future__ import annotations

from fastapi.responses import JSONResponse

from app.schemas import ErrorResponse


def error_response(status_code: int, code: str, message: str, details: dict | None = None) -> JSONResponse:
    payload = ErrorResponse(error={"code": code, "message": message, "details": details})
    return JSONResponse(status_code=status_code, content=payload.model_dump(exclude_none=True))
