from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    }
}

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )