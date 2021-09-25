import uuid


def generate_code() -> str:
    return str(uuid.uuid4()).replace('-', '').lower()[:12]
