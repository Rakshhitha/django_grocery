import math


def paginate(count, page, items):
    """
    Paginate the sql objects
    """
    # If count is 0
    if count <= 0:
        return {
            'max_page': None,
            'next_page': None,
            'previous_page': None,
            'offset': 0
        }

    # Get the max page
    max_page = math.floor(count / items)

    # If page
    if count % items >= 1:
        max_page += 1

    # Get max page if page limit is high
    if (page * items) > count:
        page = max_page

    # Get next and previous page
    next_page = None
    previous_page = None
    if page < max_page:
        next_page = page + 1
    if page > 1:
        previous_page = page - 1

    # Get the offset
    offset = 0
    if (page - 1) * items > 0:
        offset = (page - 1) * items

    return {
        'max_page': max_page,
        'next_page': next_page,
        'previous_page': previous_page,
        'offset': offset
      }