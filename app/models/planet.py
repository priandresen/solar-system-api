from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
##### check with instructors where to put this >
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .moon import Moon
##################################

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    orbital_period: Mapped[int]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")


    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self,
            "description" : self.description,
            "orbital_period" : self.orbital_period
        }

    @classmethod
    def from_dict(cls, planet_data):

        return (cls(name=planet_data['name'],
                description=planet_data['description'],
                orbital_period=planet_data['orbital_period'])
        )




