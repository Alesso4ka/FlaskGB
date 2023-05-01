from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForGet,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from blog.models.article import Article


class ArticlePermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        "id",
        "author",
        "title",
        "body",
        "dt_created",
        "dt_updated",
    ]

    PATCH_AVAILABLE_FIELDS = [
        "title",
        "body",
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        if not current_user.is_authenticated:
            raise AccessDenied("no access")
        if not current_user.is_staff:
            raise AccessDenied("no access")

        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data: dict = None, obj: Article = None, user_permission: PermissionUser = None,
                   **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)

        return {
            i_key: i_val
            for i_key, i_val in data.items()
            if i_key in permission_for_patch.columns
        }
