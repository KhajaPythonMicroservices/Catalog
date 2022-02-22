from tests.integration_tests.integration_helper import basic_test


def test_create_catalog_type(client):
    """
    This test case will test the simple post method to create a catalog type
    :param client: test client
    """
    new_catalog_item_json = {"type": "Electronics"}
    basic_test(
        client=client,
        retrieve_link="/api/v1/catalog/types",
        individual_link="/api/v1/catalog/types",
        unique_field_name='id',
        data=new_catalog_item_json
    )

