from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 100

class MyLOPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'  # created_at
