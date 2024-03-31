from src.data_base.create_db import BaseDBPart


class UpdateDB(BaseDBPart):
    async def update_feedback_status(self, feedback_id: str, status: int):
        await self.cur.execute(
            "UPDATE feedback SET status = ? WHERE feedback_id = ?",
            (status, feedback_id),
        )
        return await self.base.commit()
