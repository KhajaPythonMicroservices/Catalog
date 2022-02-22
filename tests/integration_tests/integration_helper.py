def basic_test(client,
               retrieve_link,
               individual_link,
               data,
               unique_field_name='id'):
    """ This method will test the api by creating an item

    verifying its count before and after insertion

    individual item will be retrieved and deleted

    basic assertions are added

    :param client:
    :param retrieve_link:
    :param individual_link:
    :param data:
    :param unique_field_name:
    :return:
    """
    response = client.get(retrieve_link)
    count_before_creation = len(response.json)
    response = client.post(retrieve_link, json=data)
    item_id = response.json[unique_field_name]
    assert response.status_code == 201
    response = client.get(retrieve_link)
    assert count_before_creation + 1 == len(response.json)
    # Get the specific item
    response = client.get(f"{individual_link}/{item_id}")
    assert response.status_code == 200
    # Delete the specific item
    client.delete(f"{individual_link}/{item_id}")
    response = client.get(retrieve_link)
    assert count_before_creation == len(response.json)
