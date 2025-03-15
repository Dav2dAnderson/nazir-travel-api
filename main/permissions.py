from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Admin bo'lsa (branch_admin yoki site_admin) CRUD amallar bajarishi mumkin.
    Oddiy foydalanuvchi faqat GET, HEAD, OPTIONS so‘rovlarini jo‘nata oladi.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # Bu GET, HEAD, OPTIONS bilan ishlaydi
            return True
        
        # Foydalanuvchi login qilganmi va `role` maydoni mavjudmi tekshiramiz
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'role') and
            request.user.role and
            request.user.role.name in ['branch_admin'] or request.user.is_staff
        )