from rest_framework.response import Response
from rest_framework import status as http_status


def success_response(
    *,
    data=None,
    message="Success",
    status_code=http_status.HTTP_200_OK,
    pagination=None
):
    response = {
        "status": True,
        "message": message,
        "data": data
    }

    if pagination is not None:
        response["pagination"] = pagination

    return Response(response, status=status_code)


def error_response(
    *,
    message="Error",
    errors=None,
    status_code=http_status.HTTP_400_BAD_REQUEST
):
    response = {
        "status": False,
        "message": message
    }

    if errors is not None:
        response["errors"] = errors

    return Response(response, status=status_code)
