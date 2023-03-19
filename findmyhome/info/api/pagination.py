from rest_framework.pagination import PageNumberPagination


#     Customized API pagination configurations.


class MyPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    my_offset_query_param = 'my_offset'
    offset_query_param = None