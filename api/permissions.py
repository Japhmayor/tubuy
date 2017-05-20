from rest_framework import permissions


class IsStaffOrTargetUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser or obj == request.user

class CommodityOwner(permissions.BasePermission):
    """ Custom permission to only allow commodity owners to edit it
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.requestor == request.user
