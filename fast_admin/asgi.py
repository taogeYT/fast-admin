"""
ASGI config for fast_admin project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from appboot.asgi import get_asgi_application, fastapi_register_exception

os.environ.setdefault('APP_BOOT_SETTINGS_MODULE', 'fast_admin.settings')

application = get_asgi_application()
fastapi_register_exception(application)


@application.get("/ping", summary="Health Check")
async def ping() -> str:
    return "pong"