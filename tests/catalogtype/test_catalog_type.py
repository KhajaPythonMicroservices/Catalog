
def test_create_catalog_type(client):
    """
    This test case will test the simple post method to create a catalog type
    :param client: test client
    """
    response = client.get("/api/v1/catalog/types")
    count_before_creation = len(response.json)
    new_catalog_item_json = {"type": "Electronics"}
    response = client.post("/api/v1/catalog/types", json=new_catalog_item_json)
    assert response.status_code == 201
    response = client.get("/api/v1/catalog/types")
    assert count_before_creation + 1 == len(response.json)