# Create your schema here.

from appboot import schema

from auth.models import SysOrg, SysAccount, SysRole, SysMenu


class SysOrgSchema(schema.ModelSchema):
    class Meta:
        model = SysOrg
        read_only_fields = ('created_at', 'updated_at')


class SysAccountSchema(schema.ModelSchema):
    class Meta:
        model = SysAccount
        read_only_fields = ('created_at', 'updated_at')


class SysRoleSchema(schema.ModelSchema):
    class Meta:
        model = SysRole
        read_only_fields = ('created_at', 'updated_at')


class SysMenuSchema(schema.ModelSchema):
    class Meta:
        model = SysMenu
        read_only_fields = ('created_at', 'updated_at')
