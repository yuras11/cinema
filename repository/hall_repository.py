# from orm.hall_model import HallModel, HallNameModel
# from sqlalchemy import select
# from repository.base_repository import Repository
#
#
# class HallRepository(Repository):
#     def get_all(self):
#         with self._session as session:
#             statement = select(HallModel)
#             rows = [row for row in session.scalars(statement).all()]
#             return rows
#
#
#     def get_by_id(self, hallid):
#         with self._session as session:
#             statement = select(HallModel).where(HallModel.hallid == hallid)
#             hall = session.scalars(statement).one()
#             return hall
#
#
#     def get_by_name(self, name: str):
#         with self._session as session:
#             statement = (
#                 select(HallModel)
#                 .join(HallNameModel)
#                 .where(HallNameModel.hallname == name)
#             )
#             hall = session.scalars(statement).one()
#             return hall