def get_valid_response(response, valid_responses):
    '''
    Give a list of valid responses and the response the user inputed, will continuously loop until the user
    inputs a valid response
    '''

    while str(response).lower() not in valid_responses:
        response = input("Please enter a valid response: ")
        if response in valid_responses:
            break
    return response
