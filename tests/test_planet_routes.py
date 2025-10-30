def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeeds(client, one_planet):
    # Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "rocky, blue-and-green sphere",
        "moons": 1
    }

def test_create_one_planet(client):
    # Arrange
        request_body = {
            "name": "Venus",
            "description": "a brilliant white or yellowish-white sphere",
            "moons": 0
        }

    # Act
        response = client.post("/planets", json=request_body)
        response_body = response.get_json()

        # Assert
        assert response.status_code == 201
        assert response_body == {
            "id": 1,
            "name": "Venus",
            "description": "a brilliant white or yellowish-white sphere",
            "moons": 0
        }
