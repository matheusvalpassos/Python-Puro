from sqlmodel import Field, SQLModel, create_engine, Relationship
from enum import Enum
from typing import Optional, List
from datetime import date


class Bancos(Enum):
    NUBANK = "Nubank"
    SANTANDER = "Santander"
    INTER = "Inter"


class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"


class Tipos(Enum):
    ENTRADA = "Entrada"
    SAIDA = "Saida"


class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)
    valor: float


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
