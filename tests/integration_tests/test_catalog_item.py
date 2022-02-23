from tests.integration_tests.integration_helper import basic_test


def test_catalog_item(client):
    """
    This test case will tes the catalog item
    :param client:
    :return:
    """
    new_catalog_type_json = {"type": "Laptops"}
    response = client.post("/api/v1/catalog/types", json=new_catalog_type_json)
    catalog_type_id = response.json['id']
    new_catalog_brand = {'brand': 'Apple'}
    response = client.post("/api/v1/catalog/brands", json=new_catalog_brand)
    catalog_brand_id = response.json['id']
    new_catalog_item = {
        'name': 'Apple MacBook Pro',
        'description': '13.3-inch/33.78 cm, Apple M1 chip with 8‑core CPU and 8‑core GPU, 8GB RAM, 512GB SSD',
        'price': 131990.00,
        'catalog_type_id': catalog_type_id,
        'brand_id': catalog_brand_id,
        'available_stock': 100,
        'max_stock': 500,
        'restock_threshold': 10
    }
    basic_test(
        client=client,
        individual_link='/api/v1/catalog/items',
        retrieve_link='/api/v1/catalog/items',
        unique_field_name='id',
        data=new_catalog_item
    )


def test_negative_cases_catalog_item(client):
    new_catalog_type_json = {"type": "Laptops"}
    response = client.post("/api/v1/catalog/types", json=new_catalog_type_json)
    catalog_type_id = response.json['id']
    new_catalog_brand = {'brand': 'Apple'}
    response = client.post("/api/v1/catalog/brands", json=new_catalog_brand)
    catalog_brand_id = response.json['id']
    # The data with name missing
    new_catalog_item = {
        'description': '13.3-inch/33.78 cm, Apple M1 chip with 8‑core CPU and 8‑core GPU, 8GB RAM, 512GB SSD',
        'price': 131990.00,
        'catalog_type_id': catalog_type_id,
        'brand_id': catalog_brand_id,
        'available_stock': 100,
        'max_stock': 500,
        'restock_threshold': 10
    }
    response = client.post("/api/v1/catalog/items", json=new_catalog_item)
    assert response.status_code == 400
    new_catalog_item = {
        'name': 'Apple MacBook Pro',
        'description': '13.3-inch/33.78 cm, Apple M1 chip with 8‑core CPU and 8‑core GPU, 8GB RAM, 512GB SSD',
        'price': 131990.00,
        'catalog_type_id': catalog_type_id,
        'brand_id': catalog_brand_id,
        'available_stock': 100,
        'max_stock': 500,
        'restock_threshold': 10
    }
    response = client.post("/api/v1/catalog/items", json=new_catalog_item)
    id = response.json['id']
    updated_catalog_item = {
        'description': '13.3-inch/33.78 cm, Apple M1 chip with 8‑core CPU and 8‑core GPU, 8GB RAM, 512GB SSD',
        'price': 131990.00,
        'catalog_type_id': catalog_type_id,
        'brand_id': catalog_brand_id,
        'available_stock': 1000,
        'max_stock': 500,
        'restock_threshold': 10
    }
    response = client.put(f"/api/v1/catalog/items/{id}", json=updated_catalog_item)
    assert response.status_code == 400


