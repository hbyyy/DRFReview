from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        객체의 소유자만 쓰기를 허용
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

