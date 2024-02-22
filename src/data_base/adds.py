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

    async def add_feedback(
        self,
        user_id: int,
        selection: str,
        selection_object: str,
        feedback: str,
        data_sending: int,
        stars: str,
    ):
        await self.cur.execute(
            """INSERT INTO feedback (
                        user_id, 
                        selection, 
                        selection_object, 
                        feedback, 
                        data_sending, 
                        stars
                    ) VALUES (?,?,?,?,?,?)
                """,
            (user_id, selection, selection_object, feedback, data_sending, stars),
        )
        return await self.base.commit()
