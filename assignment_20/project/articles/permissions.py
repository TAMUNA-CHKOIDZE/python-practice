from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # თუ ავტორია მხოლოდ მაშინ შეუძლია რაიმე ცვლილება
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        return True
