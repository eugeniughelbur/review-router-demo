from app.validators import safe_path

UPLOADS = "/srv/uploads"


def read_upload(name: str) -> bytes:
    with open(safe_path(UPLOADS, name), "rb") as handle:
        return handle.read()
