from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[float]
    description: Mapped[str]
    ring: Mapped[bool]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from .planet import Planet


    def to_dict(self):
        return {
            "id" : self.id,
            "size" : self.size,
            "description" : self.description,
            "ring": bool(self.ring),
            "planet_id": self.planet.id if self.planet_id else None,
            "planet_name": self.planet.name if self.planet_id else None
        }
    
    @classmethod
    def from_dict(cls, moon_data):
        return (cls(size=moon_data['size'],
                description=moon_data['description'],
                ring=moon_data['ring'],
                planet_id=moon_data.get("planet_id", None))
        )
