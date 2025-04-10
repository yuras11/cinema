from fastapi import APIRouter, Depends
from service.cast_member_service import CastMemberService
from dao.cast_member_dao import CastMemberDAO

router = APIRouter(prefix="/cast_members", tags=["Cast Members"])

# Внедряем DAO и сервис через зависимость (Dependency Injection)
def get_service():
    return CastMemberService(dao=CastMemberDAO())

# Получение актера по ID
@router.get("/{member_id}")
def get_cast_member(member_id: str, service: CastMemberService = Depends(get_service)):
    return service.get(member_id)

# Получение всех актеров
@router.get("/")
def get_all_cast_members(service: CastMemberService = Depends(get_service)):
    return service.get_all()

# Добавление нового актера
@router.post("/")
def create_cast_member(data: dict, service: CastMemberService = Depends(get_service)):
    return service.create(data)
