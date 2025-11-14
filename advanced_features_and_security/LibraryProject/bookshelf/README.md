# --- Custom Permissions and Groups Setup (Core Application) ---

# 1. Custom Permissions:
# Defined in core/models.py within the 'book' model Meta class:
# - core.can_view_book: Allows user to see book list and details.
# - core.can_create_book: Allows user to create new books.
# - core.can_edit_book: Allows user to modify existing books.
# - core.can_delete_book: Allows user to permanently remove books.

# 2. User Groups and Access Control:
# These groups are created and managed via the Django Admin interface.
# - Viewers Group: Assigned 'core.can_view_books' permission.
# - Editors Group: Assigned 'core.can_view_book', 'core.can_create_book', and 'core.can_edit_books' permissions.
# - Admins Group: Assigned all four custom permissions (and typically staff/superuser status).

# 3. Enforcement in Views:
# Views in core/views.py are protected using the @permission_required decorator.
# - book_list/detail views require 'core.can_view_book'.
# - book_create view requires 'core.can_create_book'.
# - book_edit view requires 'core.can_edit_book'.
# - book_delete view requires 'core.can_delete_book'.
# Setting 'raise_exception=True' ensures users without permission receive an HTTP 403 Forbidden response.