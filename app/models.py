from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    uquipment_id: Mapped[int] = mapped_column()
    borrower_name: Mapped[str] = mapped_column(String[70], nullable=False)
    loan_days: Mapped[str] = mapped_column(String(20), nullable=False)
    purpose: Mapped[str] = mapped_column(String(110), nullable=False)
    status: Mapped[str] = mapped_column()