from tests.integration_tests.integration_helper import basic_test


def test_catalog_brand(client):
    test_data = {'brand': 'Apple'}
    basic_test(
        client=client,
        retrieve_link="/api/v1/catalog/brands",
        individual_link="/api/v1/catalog/brands",
        data=test_data,
        unique_field_name='id'
    )
