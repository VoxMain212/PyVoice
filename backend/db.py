from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy import Integer, String, Boolean
import os


class Base(DeclarativeBase, AsyncAttrs):
    pass


class Friend(Base):
    __tablename__ = "friends"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    nickname: Mapped[str] = mapped_column(String(length=150))
    last_ip: Mapped[str] = mapped_column(String(length=50))
    user_hash: Mapped[str] = mapped_column(String(length=250))
    online: Mapped[bool] = mapped_column(Boolean(), default=False)
    avatar: Mapped[str] = mapped_column(String(length=150), nullable=True)


class Server(Base):
    __tablename__ = 'servers'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    avatar: Mapped[str] = mapped_column(String(length=150), nullable=True)
    title: Mapped[str] = mapped_column(String(length=150))
    owner_id: Mapped[int] = mapped_column(String(length=50))


class Chat(Base):
    __tablename__ = 'chats'
    
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(length=150))


async def create_tables(nickname=None):
    engine = create_async_engine(f"sqlite+aiosqlite:///{nickname}.sqlite")
    async_session = async_sessionmaker(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_session
