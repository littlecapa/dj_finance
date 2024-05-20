from django import template

register = template.Library()

def get_column_name(value):
    if value.startswith('-'):
        return value[1:]
    return value

@register.simple_tag
def toggle_sort_order(current_sort_by, current_sort_order, target_sort_by):
    print("current_sort_by ", current_sort_by, target_sort_by)
    if get_column_name(current_sort_by) == get_column_name(target_sort_by):
        return 'desc' if current_sort_order == 'asc' else 'asc'
    return 'asc'
