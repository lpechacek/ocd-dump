#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0
#
# Tool for translation of the binary .ocd format into text
# Copyright (c) 2021, Libor Pecháček.
#
# Authors:
#        Libor Pecháček <lpechacek@gmx.com>
#
# Links:
#        Source repo
#          https://github.com/lpechacek/ocd-dump

import argparse
import enum
import ocd_bootstrap
import sys
import types
from kaitaistruct import KaitaiStream

debug = False

excluded_types = (types.MethodType, types.FunctionType, types.BuiltinMethodType,
        types.BuiltinFunctionType, types.MethodWrapperType, type)
excluded_sections = []

def dump_struct(struct, name='', indent=''):
    global excluded_types
    global excluded_sections
    global print_empty
    
    members_to_print = []
    for member_name in dir(struct):
        try:
            member = getattr(struct, member_name)
        except EOFError:
            full_member_name = f'{name}{"." if name else ""}{member_name}'
            print(f'# fetch of {full_member_name} resulted in out of bounds access')
            continue

        if member_name != 'next' and member_name[0] != '_' and not isinstance(member, excluded_types):
            members_to_print.append(member_name)

    if not len(members_to_print):
        print(f'{indent}{name} not shown (type {type(struct)})')

    dump_later = []
    for member_name in members_to_print:
        full_member_name = f'{name}{"." if name else ""}{member_name}'
        if debug:
            print (f'processing {full_member_name}')

        if full_member_name in excluded_sections:
            print(f'# skipped {full_member_name}')
            continue

        member = getattr(struct, member_name)

        if isinstance(member, (int, float)) or isinstance(member, list) and (len(member) == 0 or isinstance(member[0], (int, str))):
            print(f'{indent}{full_member_name}: {member}')
        elif isinstance(member, bytes):
            print (f'{indent}{full_member_name}: bytes [' + ', '.join([f'0x{x:02X}' for x in member]) + ']')
        elif isinstance(member, str):
            print(f'{indent}{full_member_name}: ' + repr(member.rstrip('\0')))
        elif isinstance(member, parser_class.PascalString):
            print(f'{indent}{full_member_name}: {repr(member.value)}')
        elif isinstance(member, list) and isinstance(member[0], parser_class.TDPoly):
            # special handling for coords so that it does not take too much screen space
            coords_strings = []
            for element in member:
                coords_strings.append(f'[{element.x_coord},{element.y_coord},{element.flags}]')
            print(f'{indent}{full_member_name}: {", ".join(coords_strings)}')
        elif isinstance(member, parser_class.TDPoly):
            coords_string = f'[{member.x_coord},{member.y_coord},{member.flags}]'
            print(f'{indent}{full_member_name}: {coords_string}')
        elif isinstance(member, enum.Enum):
            print(f'{indent}{full_member_name}: {member.name}({member.value})')
        elif isinstance(member, list):
            print(f'{indent}{full_member_name}, {len(member)} elements')
            index = 0
            for element in member:
                if not print_empty:
                    try:
                        if not element.pos:
                            continue
                        if not element.len:
                            continue
                    except AttributeError:
                        pass
                if debug: print(f'recurse into {element}')
                dump_struct(element, f'{member_name}[{index}]', indent+'  ')
                index += 1
        else:
            dump_later.append(member_name)

    if debug:
        print(f'post-processing {dump_later}')

    for member_name in dump_later:
        member = getattr(struct, member_name)
        dump_struct(member, f'{name}{"." if name else ""}{member_name}', indent)

    try:
        if struct.next:
            dump_struct(struct.next, name, indent)
    except AttributeError:
        pass


# command line options parsing
parser = argparse.ArgumentParser(description='Dump ocd file contents in text format.')
parser.add_argument('file', type=str,
                    help='.ocd file to be processed')
parser.add_argument('--start', dest='root_member', metavar='SECTION_NAME',
                    help='start with at specified file section, e.g. \'object_index\' or \'string_index\'')
parser.add_argument('--skip', dest='excluded_sections', metavar='SECTION_NAME',
                    action='append', default=[],
                    help='skip a file section, e.g. \'object_index\' or \'string_index\'; the option can be specified multiple times')
parser.add_argument('--print-empty', dest='print_empty', action='store_true',
                    help='print empty index positions')

args = parser.parse_args()
excluded_sections = args.excluded_sections
print_empty = args.print_empty

# file processing
binary_file = open(args.file, mode='rb')
stream = KaitaiStream(binary_file)

# auto-detect the version
header_sample = ocd_bootstrap.OcdBootstrap(_io = stream)
parser_class = None
if header_sample.version == 10:
    import ocd10
    parser_class = ocd10.Ocd10
elif header_sample.version == 12:
    import ocd12
    parser_class = ocd12.Ocd12
elif header_sample.version == 2018:
    import ocd2018
    parser_class = ocd2018.Ocd2018
else:
    print(f'No parser found for version {header_sample.version}. Bailing out.')
    exit(1)

stream.seek(0)
print(f'NOTE: Using {parser_class.__name__} parser.')
testfile = parser_class(_io = stream)

# dive into the start point
root_name = []
root_struct = testfile
if args.root_member:
    for member in args.root_member.split('.'):
        root_name.append(member)
        root_struct = getattr(root_struct, member)

dump_struct(root_struct, '.'.join(root_name))

# vim:ai:et:ts=4:sw=4
