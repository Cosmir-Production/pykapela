# Supposing we are in admin.py of your own application.

# Import two helper functions and two admin models to inherit our custom model from.
from django.conf import settings
from sitetree.admin import TreeItemAdmin, TreeAdmin, override_tree_admin, override_item_admin

from django.utils.translation import ugettext_lazy as _


# This is our custom tree admin model.
class CustomTreeAdmin(TreeAdmin):
    exclude = ('title',)  # Here we exclude `title` field from form.


# And our custom tree item admin model.
class CustomTreeItemAdmin(TreeItemAdmin):
    # That will turn a tree item representation from the default variant
    # with collapsible groupings into a flat one.
    fieldsets = (
        (_('Basic settings'), {
            'fields': ('parent', 'url') + tuple('title_' + l[0] for l in settings.LANGUAGES),
        }),
        (_('Access settings'), {
            'classes': ('collapse',),
            'fields': ('access_loggedin', 'access_guest', 'access_restricted', 'access_permissions', 'access_perm_type')
        }),
        (_('Display settings'), {
            'classes': ('collapse',),
            'fields': ('hidden', 'inmenu', 'inbreadcrumbs', 'insitetree')
        }),
        (_('Additional settings'), {
            'classes': ('collapse',),
            'fields': ('hint', 'description', 'alias', 'urlaspattern')
        }),
    )

# Now we tell the SiteTree to replace generic representations with custom.
override_tree_admin(CustomTreeAdmin)
override_item_admin(CustomTreeItemAdmin)
