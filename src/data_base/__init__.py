import os
import asyncache
import aiosqlite

from src.data_base.exists import ExistDB

from src.data_base.adds import AddDB


class Database(AddDB, ExistDB):
    @classmethod
    @asyncache.cached({})
    async def setup(cls):
        if not os.path.exists("./data"):
            os.mkdir("./data")

        base = await aiosqlite.connect("data/database.db")
        cur = await base.cursor()

        if base:
            print("DATA BASE CONNECTED")

        await base.execute(
            """
            CREATE TABLE IF NOT EXISTS user(
                user_id           INTEGER NOT NULL, -- ід користувача (int)
                first_name        TEXT,             -- Ім'я користувача (str)
                last_name         TEXT,             -- Призвіще користувача (str)
                username          TEXT,             -- нікнейм користувача @ (str)
                date_join         TEXT             -- дата приєднання (дати від 1 вересня 2023) (str)
            )    
            """
        )
        await base.execute(
            """
            CREATE TABLE IF NOT EXISTS feedback(
                user_id           INTEGER NOT NULL, -- ід користувача (int)
                selection         TEXT,             -- на вибір (college, teacher, subject)
                selection_object  TEXT,             -- на вибір (None, name_teacher, name_suject)
                feedback          TEXT,             -- відгук (str)
                data_sending      INTEGER,          -- дата написання відгуку
                stars             TEXT              -- оцінка
            )
            """
        )

        await base.commit()
        return cls(base, cur)
