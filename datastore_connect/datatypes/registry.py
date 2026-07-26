import logging

from typing import Tuple, Dict
from datastore_connect.datatypes.base import TypeDef, DatastoreType, type_map
from datastore_connect.driver.exceptions import InternalError
from datastore_connect.driver.parser import parse_enum, parse_callable, parse_columns

logger = logging.getLogger(__name__)
type_cache: Dict[str, DatastoreType] = {}


def parse_name(name: str) -> Tuple[str, str, TypeDef]:
    """
    Converts a Datastore type name into the base class and the definition (TypeDef) needed for any
    additional instantiation
    :param name: Datastore type name as returned by datastore
    :return: The original base name (before arguments), the full name as passed in and the TypeDef object that
     captures any additional arguments
    """
    base = name
    wrappers = []
    keys = tuple()
    if base.startswith('LowCardinality'):
        wrappers.append('LowCardinality')
        base = base[15:-1]
    if base.startswith('Nullable'):
        wrappers.append('Nullable')
        base = base[9:-1]
    if base.startswith('Enum'):
        keys, values = parse_enum(base)
        base = base[:base.find('(')]
    elif base.startswith('Nested'):
        keys, values = parse_columns(base[6:])
        base = 'Nested'
    elif base.startswith('Tuple'):
        keys, values = parse_columns(base[5:])
        base = 'Tuple'
    elif base.startswith('Variant'):
        keys, values = parse_columns(base[7:])
        base = 'Variant'
    elif base.startswith('JSON') and len(base) > 4 and base[4] == '(':
        keys, values = parse_columns(base[4:])
        base = 'JSON'
    elif base == 'Point':
        values = ('Float64', 'Float64')
    else:
        try:
            base, values, _ = parse_callable(base)
        except IndexError:
            raise InternalError(f'Can not parse Datastore data type: {name}') from None
    return base, name, TypeDef(tuple(wrappers), keys, values)


def get_from_name(name: str) -> DatastoreType:
    """
    Returns the DatastoreType instance parsed from the Datastore type name.  Instances are cached
    :param name: Datastore type name as returned by Datastore in WithNamesAndTypes FORMAT or the Native protocol
    :return: The instance of the Datastore Type
    """
    ch_type = type_cache.get(name, None)
    if not ch_type:
        base, name, type_def = parse_name(name)
        try:
            ch_type = type_map[base].build(type_def)
        except KeyError:
            err_str = f'Unrecognized Datastore type base: {base} name: {name}'
            logger.error(err_str)
            raise InternalError(err_str) from None
        type_cache[name] = ch_type
    return ch_type
