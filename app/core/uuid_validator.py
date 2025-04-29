from uuid import UUID
from app.core.execptions import raise_bad_request_exception

def validate_uuid(uuid_to_validate):
    try:
        return UUID(uuid_to_validate)
    except:
        raise raise_bad_request_exception("Invalid UUID")