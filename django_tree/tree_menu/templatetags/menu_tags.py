from django import template
from django.urls import resolve, Resolver404

from tree_menu.models import MenuItem


register = template.Library()


def mark_active_and_expanded(items_map, current_url, current_url_name):
    """Помечаем активные и развернутые элементы."""
    active_item_found = False
    for item in items_map.values():
        if (
            item['url'] == current_url or (
                current_url_name and item['url'] == current_url_name
            )
        ):
            item['is_active'] = True
            active_item_found = True
            parent_id = item['parent_id']
            while parent_id:
                if parent_id in items_map:
                    parent = items_map[parent_id]
                    parent['is_expanded'] = True
                    parent['has_active_child'] = True
                    parent_id = parent['parent_id']
    for item in items_map.values():
        if item['is_active'] or item['has_active_child']:
            item['is_expanded'] = True
        if item['is_active']:
            for child in item['children']:
                child['is_expanded'] = True
    return active_item_found


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Построение дерева меню."""
    request = context['request']
    current_url = request.path_info
    try:
        resolved = resolve(current_url)
        current_url_name = resolved.url_name
    except Resolver404:
        current_url_name = None
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name
    ).select_related('parent')
    items_map = {}
    menu_tree = []
    for item in menu_items:
        items_map[item.id] = {
            'id': item.id,
            'name': item.name,
            'url': item.get_url(),
            'parent_id': item.parent_id,
            'children': [],
            'is_active': False,
            'is_expanded': False,
            'has_active_child': False
        }
    for item_data in items_map.values():
        parent_id = item_data['parent_id']
        if parent_id is None:
            menu_tree.append(item_data)
        else:
            if parent_id in items_map:
                items_map[parent_id]['children'].append(item_data)
    mark_active_and_expanded(items_map, current_url, current_url_name)
    if not any(item['is_active'] for item in items_map.values()):
        for item in menu_tree:
            item['is_expanded'] = True
    return {'menu_tree': menu_tree}
