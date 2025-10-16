from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # თუ ავტორია მხოლოდ მაშინ შეუძლია რაიმე ცვლილება
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.author == request.user
        # მხოლოდ სტატიის ავტორს შეუძლია შეცვლა ან წაშლა
        # if request.method in ['PUT', 'PATCH', 'DELETE']:
        #     return obj.author == request.user
        # return True  # სხვებისთვის მხოლოდ წაკითხვაა დაშვებული


