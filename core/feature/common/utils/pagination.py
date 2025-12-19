from math import ceil


def parse_pagination(request):
    """
    Supports:
    ?page=1&limit=2
    ?page=1&page_size=2
    """

    # PAGE
    try:
        page = int(request.query_params.get("page", 1))
    except (TypeError, ValueError):
        page = 1

    # LIMIT (priority) OR page_size
    try:
        limit = request.query_params.get("limit")
        if limit is not None:
            page_size = int(limit)
        else:
            page_size = int(request.query_params.get("page_size", 10))
    except (TypeError, ValueError):
        page_size = 10

    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 10

    return page, page_size


def paginate_queryset(queryset, page, page_size):
    """
    Works ONLY with Django QuerySets
    """

    total_items = queryset.count()
    total_pages = ceil(total_items / page_size) if page_size else 1

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": queryset[start:end],  # <-- HARD LIMIT HERE
        "pagination": {
            "page": page,
            "limit": page_size,
            "total_items": total_items,
            "total_pages": total_pages
        }
    }