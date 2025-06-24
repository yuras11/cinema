# from orm.cast_member_model import CastMemberModel, CastMemberNameModel
# from sqlalchemy import select
# from repository.base_repository import Repository
#
#
# class CastMemberRepository(Repository):
#     def get_by_id(self, memberid):
#         with self._session as session:
#             statement = select(CastMemberModel).where(CastMemberModel.memberid == memberid)
#             cast_member = session.scalars(statement).one()
#             return cast_member
#
#
#     def get_all(self):
#         with self._session as session:
#             statement = select(CastMemberModel)
#             rows = [row for row in session.scalars(statement).all()]
#             return rows
#
#
#     def get_by_name(self, name: str):
#         with self._session as session:
#             statement = (
#                 select(CastMemberModel)
#                 .join(CastMemberNameModel)
#                 .where(CastMemberNameModel.membername == name)
#             )
#             rows = [row for row in session.scalars(statement).all()]
#             return rows