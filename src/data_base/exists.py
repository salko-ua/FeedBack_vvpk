from src.data_base.create_db import BaseDBPart
from aiosqlite import Cursor, Row


async def exist(exist_cur: Cursor) -> bool:
    exists: Row = await exist_cur.fetchone()
    if not exists:
        return False

    return bool(exists[0])


class ExistDB(BaseDBPart):
    async def user_exists_sql(self, user_id):
        exists = await self.cur.execute(
            "SELECT COUNT(`user_id`) FROM `user` WHERE `user_id` = ?", (user_id,)
        )

        return await exist(exists)
