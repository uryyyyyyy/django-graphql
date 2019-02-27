"""
A class for storing a tree graph. Primarily used for filter constructs in the
ORM.
"""

import copy

from django.utils.hashable import make_hashable


class Node: ...