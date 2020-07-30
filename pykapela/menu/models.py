from typing import List
from sitetree.models import TreeItemBase, TreeBase


class MenuTree(TreeBase):
    pass


class MenuItem(TreeItemBase):

    def get_bottom_children(self) -> List[int]:
        """
        Returns id of the most bottom children menu items of that given
        'menu_item' tree branch
        """
        children = []
        if self.menuitem_parent.exists():
            for item in self.menuitem_parent.all():
                children += item.get_bottom_children()
        else:
            children.append(self.id)
        return children

    def get_all_menu_items_above(self) -> List[int]:
        """
        Method for getting all parent items from 'menu_item' tree branch
        including itself
        """
        parent_items = []
        if self.parent:
            parent_items += self.parent.get_all_menu_items_above()
        parent_items.append(self.id)
        return parent_items
