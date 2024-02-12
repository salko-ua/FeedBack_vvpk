from typing import Literal

from src.data_base.create_db import BaseDBPart


class AddDB(BaseDBPart):
    async def add_users_sql(
        self,
        user_id: int,
        first_name: str,
        last_name: str,
        username: str,
        date_join: str,
    ):

        await self.cur.execute(
            "INSERT INTO `user` (user_id, first_name, last_name, username, date_join) VALUES (?,?,?,?,?)",
            (user_id, first_name, last_name, username, date_join),
        )
        return await self.base.commit()
