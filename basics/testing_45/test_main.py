from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance
# TODO: Create a TestClient by passing the app to it
client = TestClient(app)


# Test function for the root endpoint
def test_read_main():
    """Test the root endpoint."""
    # TODO: Make a GET request to "/" using the client
    # TODO: Assert that the status code is 200
    # TODO: Assert that the JSON response equals {"msg": "Hello World"}
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


# Test function for the items endpoint
def test_read_item():
    """Test the items endpoint."""
    # TODO: Make a GET request to "/items/42" using the client
    # TODO: Assert that the status code is 200
    # TODO: Assert that the JSON response has correct item_id and name
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": "42", "name": "Item 42"}


# Run the tests when file is executed
if __name__ == "__main__":
    print("Running tests...")
    
    try:
        test_read_main()
        print("✓ test_read_main passed")
    except AssertionError as e:
        print(f"✗ test_read_main failed: {e}")
    except Exception as e:
        print(f"✗ test_read_main error: {e}")
    
    try:
        test_read_item()
        print("✓ test_read_item passed")
    except AssertionError as e:
        print(f"✗ test_read_item failed: {e}")
    except Exception as e:
        print(f"✗ test_read_item error: {e}")
    
    print("\nAll tests completed!")
