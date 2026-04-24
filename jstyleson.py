import json


def dispose(json_str):
    """Clear all comments in json_str.

    Clear JS-style comments like // and /**/ in json_str.
    Accept a str or unicode as input.

    Args:
        json_str: A json string of str or unicode to clean up comment

    Returns:
        str: The str without comments (or unicode if you pass in unicode)
    """
    pass


# There may be performance suffer backtracking the last comma
def _remove_last_comma(str_list, before_index):
    pass


# Below are just some wrapper function around the standard json module.

def loads(text, **kwargs):
    pass


def load(fp, **kwargs):
    pass


def dumps(obj, **kwargs):
    pass


def dump(obj, fp, **kwargs):
    pass
