class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons

planets = [
    Planet(1, 'Mercury', 'shiny, silver-white, and metallic.', 0),
    Planet(2, 'Earth', 'rocky, blue-and-green sphere', 1),
    Planet(3, 'Jupiter', 'colorful cloud bands, which are a mix of red, brown, yellow, and white', 95),
    Planet(4, 'Mars', 'rocky, desert-like world with a, dry surface', 2),
    Planet(5, 'Saturn', 'a pale, yellowish-brown gas giant with prominent rings', 146),
    Planet(6, 'Uranus', 'gaseous cyan-coloured ice giant', 28),   
    Planet(7, 'Neptune', 'deep, blue gas giant planet with a dynamic atmosphere', 14),
    Planet(8, 'Venus', 'a brilliant white or yellowish-white sphere', 0)
]