from src.data_base.create_db import BaseDBPart


class SelectDB(BaseDBPart):
    # приклад методу для витягування з бази даних кількість користувачі
    # метод нічого не приймає, а повертає число від 0 до ...
    async def count_users(self) -> int:
        result = await self.cur.execute("SELECT COUNT(user_id) FROM user")
        result = await result.fetchone()
        return result[0]
