from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'