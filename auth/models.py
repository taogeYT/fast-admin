# Create your models here.

from appboot import models
from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Model(models.Model, models.TimestampMixin, models.DeletedAtMixin):
    __abstract__ = True


class SysOrg(Model):
    name: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[Optional[str]] = mapped_column(nullable=True)
    level: Mapped[Optional[int]] = mapped_column(nullable=True)
    org_type: Mapped[Optional[str]] = mapped_column(nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(nullable=True)
    status: Mapped[int] = mapped_column(nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(nullable=True)


class SysAccount(Model):
    username: Mapped[str] = mapped_column(unique=True)
    nickname: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[Optional[str]] = None
    avatar: Mapped[Optional[str]] = None
    sex: Mapped[bool]
    status: Mapped[int]
    birthday: Mapped[Optional[datetime]] = None
    org_id: Mapped[Optional[int]]


class SysRole(Model):
    name: Mapped[str]
    code: Mapped[Optional[str]] = None
    data_scope: Mapped[int] = mapped_column(default=1)
    remark: Mapped[Optional[str]] = None
    status: Mapped[int]


class SysMenu(Model):
    type: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    path: Mapped[Optional[str]] = mapped_column(nullable=True)
    component: Mapped[Optional[str]] = mapped_column(nullable=True)
    redirect: Mapped[Optional[str]] = mapped_column(nullable=True)
    permission: Mapped[Optional[str]] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(nullable=False)
    icon: Mapped[Optional[str]] = mapped_column(nullable=True)
    is_iframe: Mapped[bool] = mapped_column(nullable=False)
    out_link: Mapped[Optional[str]] = mapped_column(nullable=True)
    is_hide: Mapped[bool] = mapped_column(nullable=False)
    is_keep_alive: Mapped[bool] = mapped_column(nullable=False)
    is_affix: Mapped[bool] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False)
    remark: Mapped[Optional[str]] = mapped_column(nullable=True)
    parent_id: Mapped[Optional[int]] = mapped_column(nullable=True)


# relationship
class SysAccountRole(Model):
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey('sys_account.id'))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('sys_role.id'))


class SysRoleMenu(Model):
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('sys_role.id'))
    menu_id: Mapped[int] = mapped_column(Integer, ForeignKey('sys_menu.id'))
