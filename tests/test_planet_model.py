from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(name="Earth",
                    description="rocky, blue-and-green sphere",
                    orbital_period=365)

    # Act
    result = test_data.to_dict()

    # Assert
    #assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Earth"
    assert result["description"] == "rocky, blue-and-green sphere"
    assert result["orbital_period"] == 365

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Earth",
                    description="rocky, blue-and-green sphere",
                    orbital_period=365)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Earth"
    assert result["description"] == "rocky, blue-and-green sphere"
    assert result["orbital_period"] == 365
def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="rocky, blue-and-green sphere")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "rocky, blue-and-green sphere"
    assert result["orbital_period"] == 365
def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The Best!"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "Rocky",
        "orbital_period": 100
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Pluto",
        "orbital_period": 0
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best!",
        "another": "last value",
        "orbital_period": 0
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"