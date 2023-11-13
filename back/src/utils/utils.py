from flask import request, jsonify

from src.strings import API


def server_error(message, will_exit=False):
    """
    Server error
    :param will_exit: Boolean - Example : server("Something went wrong", True)
    :param message: String - Example : server("Something went wrong")
    """

    print('\033[31m\033[4m' + f"SERVER ERROR : {message}" + '\033[30m\033[0m')

    if will_exit:
        exit(1)


def response(response_value, content, code=API.SUCCESS):
    """
    Response
    :param code: API - Example : response(JOHN.OK, "Everything is fine", API.BAD_REQUEST)
    :param response_value: JOHN - Example : response(JOHN.OK, "Everything is fine")
    :param content: String - Example : response(JOHN.DB_ERROR, "Everything is not fine")

    """

    if code.value != 200:
        print('\033[1;33m\033[1m' + "Endpoint : " + str(request.url) + '\033[30m\033[0m')
        print('\033[1;33m\033[1m' + str(code.value) + " - " + str(response_value) + " : " + str(
            content) + '\033[30m\033[0m')
        return jsonify(
            {
                "response": "KO",
                "content": content
            }
        ), code.value

    print('\033[32m\033[1m' + "Endpoint : " + str(request.url) + '\033[30m\033[0m')
    print('\033[32m\033[1m' + str(code.value) + " - OK" + '\033[30m\033[0m')
    return jsonify(
        {
            "response": "OK",
            "content": content
        }
    ), code.value
