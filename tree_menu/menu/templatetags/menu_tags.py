from typing import Dict, List

from django import template

from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, main_menu) -> List[Dict[str, any]]:
    """
    Отображает меню на основе переданного контекста и имени меню.

    Аргументы:
    context (dict): Контекст шаблона, содержащий информацию о запросе.
    menu (str): Имя меню для отображения.

    Возвращает:
    List[Dict[str, any]]: Список словарей, представляющих элементы меню для отображения.
    """
    items = MenuItem.objects.all()
    root_parents = list(items.filter(parent=None).values())

    try:
        cur_item = items.get(id=context['request'].GET[main_menu])
    except Exception:
        return {'items': root_parents, 'menu': main_menu}

    object_parents = get_all_parents_child(cur_item)

    for parent in root_parents:
        if parent['id'] in object_parents:
            parent['child_items'] = get_child_items(
                parent['id'], object_parents, items
            )

    result_dict = {'items': root_parents}
    result_dict['menu'] = main_menu
    result_dict['cur_id'] = cur_item.id

    return result_dict


def get_all_parents_child(parent: MenuItem) -> List[int]:
    """
    Получаем все родительские элементы объекта, включая сам объект.
    
    Аргументы:
    parent (MenuItem): Объект, для которого нужно получить всех родителей.
    
    Возвращает:
    List[int]: Список идентификаторов всех родительских элементов объекта, включая сам объект.
    """
    items_id_list = []
    while parent:
        items_id_list.append(parent.id)
        parent = parent.parent
    return items_id_list


def get_child_items(
        cur_parent_id: int, object_parents: List[int], items: list[MenuItem]
) -> List[Dict[str, any]]:
    """
    Получаем дочерние элементы для указанного родительского элемента.

    Аргументы:
    cur_parent_id (int): Идентификатор текущего родительского элемента.
    object_parents (List[int]): Список идентификаторов всех родительских элементов.
    items (list[MenuItem]): Список всех элементов меню.

    Возвращает:
    List[Dict[str, any]]: Список дочерних элементов для указанного родительского элемента.
    """

    cur_children = list(items.filter(parent_id=cur_parent_id).values())

    for child in cur_children:
        if child['id'] in object_parents:
            child['child_items'] = get_child_items(
                child['id'], object_parents, items
            )

    return cur_children
