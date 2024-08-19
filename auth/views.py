# Create your api here.
from appboot import PaginationResult, QueryDepends, QuerySchema
from appboot.db import create_tables
from fastapi import APIRouter, Depends

from auth.schema import SysOrgSchema, SysRoleSchema
from auth.models import SysOrg, SysRole

router = APIRouter(dependencies=[Depends(create_tables)])


@router.post("/login/account")
async def login():
    return {"status": "ok", "type": "account", "currentAuthority": "admin"}


@router.get("/currentUser")
async def login():
    return {
        "success": True,
        "data": {
            "name": "admin",
            "avatar": "https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png",
            "userid": "00000001",
            "email": "antdesign@alipay.com",
            "signature": "海纳百川，有容乃大",
            "title": "交互专家",
            "group": "蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED",
            "tags": [
                {
                    "key": "0",
                    "label": "很有想法的"
                },
                {
                    "key": "1",
                    "label": "专注设计"
                },
                {
                    "key": "2",
                    "label": "辣~"
                },
                {
                    "key": "3",
                    "label": "大长腿"
                },
                {
                    "key": "4",
                    "label": "川妹子"
                },
                {
                    "key": "5",
                    "label": "海纳百川"
                }
            ],
            "notifyCount": 12,
            "unreadCount": 11,
            "country": "China",
            "access": "admin",
            "geographic": {
                "province": {
                    "label": "浙江省",
                    "key": "330000"
                },
                "city": {
                    "label": "杭州市",
                    "key": "330100"
                }
            },
            "address": "西湖区工专路 77 号",
            "phone": "0752-268888888"
        }
    }


@router.get("/org", response_model=PaginationResult[SysOrgSchema])
async def get_org(query: QuerySchema = QueryDepends()):
    return await query.query_result(SysOrg.objects.clone())


@router.post("/org", response_model=SysOrgSchema)
async def create_org(data: SysOrgSchema):
    return await data.create()


@router.get("/role", response_model=PaginationResult[SysRoleSchema])
async def get_org(query: QuerySchema = QueryDepends()):
    return await query.query_result(SysRole.objects.clone())


@router.post("/role", response_model=SysRoleSchema)
async def create_org(data: SysRoleSchema):
    return await data.create()


@router.put("/role/{pk}", response_model=SysRoleSchema)
async def update_org(pk: int, data: SysRoleSchema):
    instance = await SysRole.objects.get(pk)
    await data.update(instance)
    print(instance)
    return instance
