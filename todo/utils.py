def form_filter_request(filter_fields):
    filters = ''
    c = 0
    for field, value in filter_fields.items():
        if c == 0:
            filters += f' WHERE {field}="{value}"'
        else:
            filters += f' AND {field}="{value}"'
        c += 1
    return filters
