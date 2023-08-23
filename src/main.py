from fastapi import FastAPI
from starlette.config import Config
from app.router import router as appRouter

# config = Config(".env")
#
# ENVIRONMENT = config("ENVIRONMENT")
# SHOW_DOCS_ENVIRONMENT = ("lcoal","staging")
#
# app_config = {"title":"My Cool API"}
# if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
#     app_config["openapi_url"] = None

# app = FastAPI(**app_config)
app = FastAPI()
app.router.include_router(appRouter,prefix="/app")
