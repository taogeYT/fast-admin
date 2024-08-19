"""
API Router configuration for fast_admin project.

Examples:
    from fastapi import APIRouter
    from myapp import views

    root_router = APIRouter()
    root_router.include_router(views.router, tags=["demo"])
"""
from fastapi import APIRouter
from auth import views as auth_views

root_router = APIRouter(prefix="/api")
root_router.include_router(auth_views.router, tags=["Auth"])
