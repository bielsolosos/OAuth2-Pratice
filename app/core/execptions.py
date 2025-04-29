from fastapi import HTTPException

def raise_not_found_exception(detail: str = "Resource not found"):
    """retorna 404 com a mensagem selecionada"""
    raise HTTPException(status_code=404, detail=detail)

def raise_bad_request_exception(detail: str = "Bad request"):
    """retorna 400 com a mensagem selecionada"""
    raise HTTPException(status_code=400, detail=detail)

def raise_internal_server_error(detail: str = "An unexpected error occurred"):
    """retorna 400 com a mensagem selecionada"""
    raise HTTPException(status_code=500, detail=detail)

def raise_created_exception(detail: str = "Resource created successfully"):
    """retorna 201 com a mensagem selecionada"""
    raise HTTPException(status_code=201, detail=detail)

def raise_accepted_exception(detail: str = "Request accepted"):
    """retorna 202 com a mensagem selecionada"""
    raise HTTPException(status_code=202, detail=detail)