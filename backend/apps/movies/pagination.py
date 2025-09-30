from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MoviePagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = 100
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'items': data,
            'page': self.page.number,
            'limit': self.get_page_size(self.request) or self.page.paginator.per_page,
            'total': self.page.paginator.count,
        })


