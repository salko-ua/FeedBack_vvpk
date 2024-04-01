from src.data_base.create_db import BaseDBPart


class SelectDB(BaseDBPart):
    # приклад методу для витягування з бази даних кількість користувачі
    # метод нічого не приймає, а повертає число від 0 до ...
    async def count_users(self) -> int:
        result = await self.cur.execute("SELECT COUNT(user_id) FROM user")
        result = await result.fetchone()
        return result[0]

    async def count_accept_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE status = ?",
            (1,),
        )
        result = await result.fetchone()
        return result[0]

    async def count_reject_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE status = ?",
            (2,),
        )
        result = await result.fetchone()
        return result[0]

    async def count_accept_reject_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE status IN (?, ?)",
            (1, 2),
        )
        result = await result.fetchone()
        return result[0]

    async def count_teacher_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE selection = ? AND status IN (?, ?)",
            ("teacher", 1, 2),
        )
        result = await result.fetchone()
        return result[0]

    async def count_subject_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE selection = ? AND status IN (?, ?)",
            ("subject", 1, 2),
        )
        result = await result.fetchone()
        return result[0]

    async def count_college_feedback(self):
        result = await self.cur.execute(
            "SELECT COUNT(feedback_id) FROM feedback WHERE selection = ? AND status IN (?, ?)",
            ("collage", 1, 2),
        )
        result = await result.fetchone()
        return result[0]

    async def get_feedback(self, feedback_id: str):
        result = await self.cur.execute(
            "SELECT * FROM feedback WHERE feedback_id = ?",
            (feedback_id,),
        )
        result = await result.fetchone()
        return result

    async def get_feedback_by_selection(self, selection: str, count: int):
        offset = (count - 1) * 5

        result = await self.cur.execute(
            "SELECT feedback_id, feedback FROM feedback WHERE selection = ? LIMIT 5 OFFSET ?",
            (selection, offset),
        )
        result = await result.fetchall()
        return result
