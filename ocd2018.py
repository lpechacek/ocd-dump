# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ocd2018(KaitaiStruct):

    class EObjectStringType(Enum):
        none = 0
        course_setting_object = 1
        course_setting_preview_object = 2
        course_setting_layout_object = 3
        course_setting_thematic_object = 4

    class EObjectStatus(Enum):
        deleted_no_undo = 0
        normal = 1
        hidden = 2
        deleted_for_undo = 3

    class ESymbolElementType(Enum):
        line = 1
        area = 2
        circle = 3
        dot = 4

    class EAreaStructMode(Enum):
        none = 0
        aliged_rows = 1
        shifted_rows = 2

    class EObjEtSymTypes(Enum):
        point = 1
        line = 2
        area = 3
        text = 4
        line_text = 6
        rectangle = 7

    class EAreaHatchMode(Enum):
        none = 0
        single_hatch = 1
        cross_hatch = 2

    class EStructDrawingMode(Enum):
        clip = 0
        completely_inside = 1
        center_inside = 2
        partially_inside = 3

    class EFileType(Enum):
        normal_map = 0
        course_setting_project = 1
        server_stored_file = 8

    class EObjectViewMode(Enum):
        normal = 0
        course_setting_object = 1
        modified_preview_onject = 2
        unmodified_preview_object = 3
        temporary_object = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_header = Ocd2018.OcdFileHeader(self._io, self, self._root)

    class TTextSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_font_name = self._io.read_bytes(32)
            _io__raw_font_name = KaitaiStream(BytesIO(self._raw_font_name))
            self.font_name = Ocd2018.PascalString(_io__raw_font_name, self, self._root)
            self.font_color = self._io.read_u2le()
            self.font_size = self._io.read_u2le()
            self.weight = self._io.read_u2le()
            self.italic = self._io.read_u1()
            self.reserved1 = self._io.read_bytes(1)
            self.char_space = self._io.read_u2le()
            self.word_space = self._io.read_u2le()
            self.alignment = self._io.read_u2le()
            self.line_space = self._io.read_u2le()
            self.para_space = self._io.read_u2le()
            self.indent_first = self._io.read_u2le()
            self.indent_other = self._io.read_u2le()
            self.n_tabs = self._io.read_u2le()
            self.tabs = [None] * (32)
            for i in range(32):
                self.tabs[i] = self._io.read_u4le()

            self.lbon = self._io.read_u2le()
            self.lbcolor = self._io.read_u2le()
            self.lbwidth = self._io.read_u2le()
            self.lbdist = self._io.read_u2le()
            self.reserved2 = self._io.read_bytes(2)
            self.fr_mode = self._io.read_u1()
            self.fr_line_style = self._io.read_u1()
            self.point_sym_on = self._io.read_u1()
            self.point_sym_number = self._io.read_u4le()
            self.reserved3 = self._io.read_bytes(19)
            self.fr_left = self._io.read_u2le()
            self.fr_bottom = self._io.read_u2le()
            self.fr_right = self._io.read_u2le()
            self.fr_top = self._io.read_u2le()
            self.fr_color = self._io.read_u2le()
            self.fr_width = self._io.read_u2le()
            self.reserved4 = self._io.read_bytes(2)
            self.reserved5 = self._io.read_bytes(2)
            self.fr_of_x = self._io.read_u2le()
            self.fr_of_y = self._io.read_u2le()


    class TSymbolBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4le()
            self.sym_num = self._io.read_u4le()
            self.otp = KaitaiStream.resolve_enum(Ocd2018.EObjEtSymTypes, self._io.read_u1())
            self.flags = self._io.read_u1()
            self.selected = self._io.read_u1()
            self.status = self._io.read_u1()
            self.drawing_tool = self._io.read_u1()
            self.cs_mode = self._io.read_u1()
            self.cs_objtype = self._io.read_u1()
            self.cs_cdflags = self._io.read_u1()
            self.extent = self._io.read_u4le()
            self.file_pos = self._io.read_u4le()
            self.reserved1 = self._io.read_bytes(2)
            self.n_colors = self._io.read_u2le()
            self.colors = [None] * (14)
            for i in range(14):
                self.colors[i] = self._io.read_u2le()

            self.description = (self._io.read_bytes(128)).decode(u"UTF-16LE")
            self.icon_bits = self._io.read_bytes(484)
            self.symbol_tree_group = [None] * (64)
            for i in range(64):
                self.symbol_tree_group[i] = self._io.read_u2le()



    class TSymElt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.st_type = KaitaiStream.resolve_enum(Ocd2018.ESymbolElementType, self._io.read_u2le())
            self.st_flags = self._io.read_u2le()
            self.st_color = self._io.read_u2le()
            self.st_line_width = self._io.read_u2le()
            self.st_diameter = self._io.read_u2le()
            self.st_n_poly = self._io.read_u2le()
            self.reserved1 = self._io.read_bytes(4)
            self._raw_st_poly = self._io.read_bytes((self.st_n_poly * 8))
            _io__raw_st_poly = KaitaiStream(BytesIO(self._raw_st_poly))
            self.st_poly = Ocd2018.TSymElementPoly(_io__raw_st_poly, self, self._root)


    class TLineTextSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_font_name = self._io.read_bytes(32)
            _io__raw_font_name = KaitaiStream(BytesIO(self._raw_font_name))
            self.font_name = Ocd2018.PascalString(_io__raw_font_name, self, self._root)
            self.font_color = self._io.read_u2le()
            self.font_size = self._io.read_u2le()
            self.weight = self._io.read_u2le()
            self.italic = self._io.read_u1()
            self.reserved1 = self._io.read_bytes(1)
            self.char_space = self._io.read_u2le()
            self.word_space = self._io.read_u2le()
            self.alignment = self._io.read_u2le()
            self.fr_mode = self._io.read_u1()
            self.fr_line_style = self._io.read_u1()
            self.reserved2 = self._io.read_bytes(32)
            self.fr_color = self._io.read_u2le()
            self.fr_width = self._io.read_u2le()
            self.reserved3 = self._io.read_bytes(4)
            self.fr_of_x = self._io.read_u2le()
            self.fr_of_y = self._io.read_u2le()


    class TAreaSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.border_sym = self._io.read_u4le()
            self.fill_color = self._io.read_u2le()
            self.hatch_mode = KaitaiStream.resolve_enum(Ocd2018.EAreaHatchMode, self._io.read_u2le())
            self.hatch_color = self._io.read_u2le()
            self.hatch_line_width = self._io.read_u2le()
            self.hatch_dist = self._io.read_u2le()
            self.hatch_angle1 = self._io.read_u2le()
            self.hatch_angle2 = self._io.read_u2le()
            self.fill_on = self._io.read_u1()
            self.border_on = self._io.read_u1()
            self.struct_mode = KaitaiStream.resolve_enum(Ocd2018.EAreaStructMode, self._io.read_u1())
            self.struct_draw = KaitaiStream.resolve_enum(Ocd2018.EStructDrawingMode, self._io.read_u1())
            self.struct_width = self._io.read_u2le()
            self.struct_height = self._io.read_u2le()
            self.struct_angle = self._io.read_u2le()
            self.struct_irregular_var_x = self._io.read_u1()
            self.struct_irregular_var_y = self._io.read_u1()
            self.struct_irregular_min_dist = self._io.read_u2le()
            self.reserved1 = self._io.read_bytes(2)
            self.data_size = self._io.read_u2le()
            if self.data_size > 0:
                self._raw_elements = self._io.read_bytes((self.data_size * 8))
                _io__raw_elements = KaitaiStream(BytesIO(self._raw_elements))
                self.elements = Ocd2018.TSymElements(_io__raw_elements, self, self._root)



    class TDPoly(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x_value = self._io.read_s4le()
            self.y_value = self._io.read_s4le()

        @property
        def flags(self):
            if hasattr(self, '_m_flags'):
                return self._m_flags if hasattr(self, '_m_flags') else None

            self._m_flags = ((self.x_value & 15) | (self.y_value & (15 << 4)))
            return self._m_flags if hasattr(self, '_m_flags') else None

        @property
        def x_coord(self):
            if hasattr(self, '_m_x_coord'):
                return self._m_x_coord if hasattr(self, '_m_x_coord') else None

            self._m_x_coord = self.x_value // 256
            return self._m_x_coord if hasattr(self, '_m_x_coord') else None

        @property
        def y_coord(self):
            if hasattr(self, '_m_y_coord'):
                return self._m_y_coord if hasattr(self, '_m_y_coord') else None

            self._m_y_coord = self.y_value // 256
            return self._m_y_coord if hasattr(self, '_m_y_coord') else None


    class PascalString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u1()
            self.data = (self._io.read_bytes(self.len)).decode(u"ISO8859-1")

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = self.data
            return self._m_value if hasattr(self, '_m_value') else None


    class TSymbolPos(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pos = self._io.read_u4le()

        @property
        def symbol(self):
            if hasattr(self, '_m_symbol'):
                return self._m_symbol if hasattr(self, '_m_symbol') else None

            if self.pos > 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.pos)
                self._m_symbol = Ocd2018.TSymbol(io, self, self._root)
                io.seek(_pos)

            return self._m_symbol if hasattr(self, '_m_symbol') else None


    class TLineSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.line_color = self._io.read_u2le()
            self.line_width = self._io.read_u2le()
            self.line_style = self._io.read_u2le()
            self.dist_from_start = self._io.read_u2le()
            self.dist_to_end = self._io.read_u2le()
            self.main_length = self._io.read_u2le()
            self.end_length = self._io.read_u2le()
            self.main_gap = self._io.read_u2le()
            self.sec_gap = self._io.read_u2le()
            self.end_gap = self._io.read_u2le()
            self.min_sym = self._io.read_u2le()
            self.n_prim_sym = self._io.read_u2le()
            self.prim_sym_dist = self._io.read_u2le()
            self.dbl_mode = self._io.read_u2le()
            self.dbl_flags = self._io.read_u2le()
            self.dbl_fill_color = self._io.read_u2le()
            self.dbl_left_color = self._io.read_u2le()
            self.dbl_right_color = self._io.read_u2le()
            self.dbl_width = self._io.read_u2le()
            self.dbl_left_width = self._io.read_u2le()
            self.dbl_right_width = self._io.read_u2le()
            self.dbl_length = self._io.read_u2le()
            self.dbl_gap = self._io.read_u2le()
            self.reserved1 = self._io.read_bytes(6)
            self.dec_mode = self._io.read_u2le()
            self.dec_symbol_size = self._io.read_u2le()
            self.dec_symbol_distance = self._io.read_u1()
            self.dec_symbol_width = self._io.read_u1()
            self.fr_color = self._io.read_u2le()
            self.fr_width = self._io.read_u2le()
            self.fr_style = self._io.read_u2le()
            self.prim_dsize = self._io.read_u2le()
            self.sec_dsize = self._io.read_u2le()
            self.corner_dsize = self._io.read_u2le()
            self.start_dsize = self._io.read_u2le()
            self.end_dsize = self._io.read_u2le()
            self.use_symbol_flags = self._io.read_u1()
            self.reserved = self._io.read_u1()
            if self.prim_dsize > 0:
                self._raw_prim_elements = self._io.read_bytes((self.prim_dsize * 8))
                _io__raw_prim_elements = KaitaiStream(BytesIO(self._raw_prim_elements))
                self.prim_elements = Ocd2018.TSymElements(_io__raw_prim_elements, self, self._root)

            if self.sec_dsize > 0:
                self._raw_sec_elements = self._io.read_bytes((self.sec_dsize * 8))
                _io__raw_sec_elements = KaitaiStream(BytesIO(self._raw_sec_elements))
                self.sec_elements = Ocd2018.TSymElements(_io__raw_sec_elements, self, self._root)

            if self.corner_dsize > 0:
                self._raw_corner_elements = self._io.read_bytes((self.corner_dsize * 8))
                _io__raw_corner_elements = KaitaiStream(BytesIO(self._raw_corner_elements))
                self.corner_elements = Ocd2018.TSymElements(_io__raw_corner_elements, self, self._root)

            if self.start_dsize > 0:
                self._raw_start_elements = self._io.read_bytes((self.start_dsize * 8))
                _io__raw_start_elements = KaitaiStream(BytesIO(self._raw_start_elements))
                self.start_elements = Ocd2018.TSymElements(_io__raw_start_elements, self, self._root)

            if self.end_dsize > 0:
                self._raw_end_elements = self._io.read_bytes((self.end_dsize * 8))
                _io__raw_end_elements = KaitaiStream(BytesIO(self._raw_end_elements))
                self.end_elements = Ocd2018.TSymElements(_io__raw_end_elements, self, self._root)



    class TSymElementPoly(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(Ocd2018.TDPoly(self._io, self, self._root))
                i += 1



    class TSymElements(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(Ocd2018.TSymElt(self._io, self, self._root))
                i += 1



    class TStringIndexBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.next_index_block = self._io.read_u4le()
            self.string_table = [None] * (256)
            for i in range(256):
                self.string_table[i] = Ocd2018.TStringIndex(self._io, self, self._root)


        @property
        def next(self):
            if hasattr(self, '_m_next'):
                return self._m_next if hasattr(self, '_m_next') else None

            if self.next_index_block != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.next_index_block)
                self._m_next = Ocd2018.TStringIndexBlock(io, self, self._root)
                io.seek(_pos)

            return self._m_next if hasattr(self, '_m_next') else None


    class TSymbolIndexBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.next_index_block = self._io.read_u4le()
            self.symbol_position = [None] * (256)
            for i in range(256):
                self.symbol_position[i] = Ocd2018.TSymbolPos(self._io, self, self._root)


        @property
        def next(self):
            if hasattr(self, '_m_next'):
                return self._m_next if hasattr(self, '_m_next') else None

            if self.next_index_block != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.next_index_block)
                self._m_next = Ocd2018.TSymbolIndexBlock(io, self, self._root)
                io.seek(_pos)

            return self._m_next if hasattr(self, '_m_next') else None


    class OcdFileHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\xAD\x0C":
                raise kaitaistruct.ValidationNotEqualError(b"\xAD\x0C", self.magic, self._io, u"/types/ocd_file_header/seq/0")
            self.file_type = KaitaiStream.resolve_enum(Ocd2018.EFileType, self._io.read_u1())
            self.file_status = self._io.read_u1()
            self.version = self._io.read_u2le()
            self.sub_version = self._io.read_u1()
            self.sub_sub_version = self._io.read_u1()
            self.first_symbol_index_block = self._io.read_u4le()
            self.first_object_index_block = self._io.read_u4le()
            self.offline_sync_serial = self._io.read_u4le()
            self.current_file_version = self._io.read_u4le()
            self.reserved1 = self._io.read_bytes(8)
            self.first_string_index_block = self._io.read_u4le()
            self.file_name_pos = self._io.read_u4le()
            self.file_name_size = self._io.read_u4le()
            self.reserved2 = self._io.read_bytes(12)
            self.first_mr_index_block = self._io.read_u4le()


    class TObjectIndexBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.next_index_block = self._io.read_u4le()
            self.object_table = [None] * (256)
            for i in range(256):
                self.object_table[i] = Ocd2018.TObjectIndex(self._io, self, self._root)


        @property
        def next(self):
            if hasattr(self, '_m_next'):
                return self._m_next if hasattr(self, '_m_next') else None

            if self.next_index_block != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.next_index_block)
                self._m_next = Ocd2018.TObjectIndexBlock(io, self, self._root)
                io.seek(_pos)

            return self._m_next if hasattr(self, '_m_next') else None


    class TObjectIndex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rc = [None] * (2)
            for i in range(2):
                self.rc[i] = Ocd2018.TDPoly(self._io, self, self._root)

            self.pos = self._io.read_u4le()
            self.len = self._io.read_u4le()
            self.sym = self._io.read_s4le()
            self.obj_type = KaitaiStream.resolve_enum(Ocd2018.EObjEtSymTypes, self._io.read_u1())
            self.encrypted_mode = self._io.read_u1()
            self.status = KaitaiStream.resolve_enum(Ocd2018.EObjectStatus, self._io.read_u1())
            self.view_type = KaitaiStream.resolve_enum(Ocd2018.EObjectViewMode, self._io.read_u1())
            self.color = self._io.read_s2le()
            self.group = self._io.read_s2le()
            self.imp_layer = self._io.read_s2le()
            self.reserved1 = self._io.read_bytes(2)

        @property
        def object(self):
            """I'm not sure if the entry:element is 1:1 relationship.
            Verify that there cannot be more TElement structures packed in
            the space reserved by t_object_index.len."""
            if hasattr(self, '_m_object'):
                return self._m_object if hasattr(self, '_m_object') else None

            _pos = self._io.pos()
            self._io.seek(self.pos)
            self._raw__m_object = self._io.read_bytes(self.len)
            _io__raw__m_object = KaitaiStream(BytesIO(self._raw__m_object))
            self._m_object = Ocd2018.TElement(_io__raw__m_object, self, self._root)
            self._io.seek(_pos)
            return self._m_object if hasattr(self, '_m_object') else None


    class TSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base = Ocd2018.TSymbolBase(self._io, self, self._root)
            _on = self.base.otp
            if _on == Ocd2018.EObjEtSymTypes.text:
                self.type_specific = Ocd2018.TTextSymbol(self._io, self, self._root)
            elif _on == Ocd2018.EObjEtSymTypes.line_text:
                self.type_specific = Ocd2018.TLineTextSymbol(self._io, self, self._root)
            elif _on == Ocd2018.EObjEtSymTypes.rectangle:
                self.type_specific = Ocd2018.TRectangleSymbol(self._io, self, self._root)
            elif _on == Ocd2018.EObjEtSymTypes.line:
                self.type_specific = Ocd2018.TLineSymbol(self._io, self, self._root)
            elif _on == Ocd2018.EObjEtSymTypes.area:
                self.type_specific = Ocd2018.TAreaSymbol(self._io, self, self._root)
            elif _on == Ocd2018.EObjEtSymTypes.point:
                self.type_specific = Ocd2018.TPointSymbol(self._io, self, self._root)


    class TElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sym = self._io.read_s4le()
            self.otp = KaitaiStream.resolve_enum(Ocd2018.EObjEtSymTypes, self._io.read_u1())
            self.reserved1 = self._io.read_bytes(1)
            self.ang = self._io.read_s2le()
            self.color = self._io.read_u4le()
            self.line_width = self._io.read_s2le()
            self.diam_flags = self._io.read_s2le()
            self.server_object_id = self._io.read_u4le()
            self.height = self._io.read_u4le()
            self.creation_date = self._io.read_f8le()
            self.multirepresentation_id = self._io.read_u4le()
            self.modification_date = self._io.read_f8le()
            self.n_item = self._io.read_u4le()
            self.n_text = self._io.read_u2le()
            self.n_object_string = self._io.read_u2le()
            self.n_database_string = self._io.read_u2le()
            self.object_string_type = KaitaiStream.resolve_enum(Ocd2018.EObjectStringType, self._io.read_u1())
            self.reserved2 = self._io.read_bytes(1)
            if  ((self.n_item != 0) and (self.otp.value != 1)) :
                self.poly = [None] * (self.n_item)
                for i in range(self.n_item):
                    self.poly[i] = Ocd2018.TDPoly(self._io, self, self._root)


            if self.otp.value == 1:
                self.center = Ocd2018.TDPoly(self._io, self, self._root)

            if  ((self.n_item > 1) and (self.otp.value == 1)) :
                self.cut_angles = [None] * ((self.n_item - 1))
                for i in range((self.n_item - 1)):
                    self.cut_angles[i] = Ocd2018.PointSymbolCutAngle(self._io, self, self._root)


            if self.n_text != 0:
                self.text = (self._io.read_bytes((self.n_text * 8))).decode(u"UTF-16LE")



    class PointSymbolCutAngle(KaitaiStruct):
        """Cut angles in tenths of degrees."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start_deg = self._io.read_s4le()
            self.end_deg = self._io.read_s4le()


    class TRectangleSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.line_color = self._io.read_u2le()
            self.line_width = self._io.read_u2le()
            self.radius = self._io.read_u2le()
            self.grid_flags = self._io.read_u2le()
            self.cell_width = self._io.read_u2le()
            self.cell_height = self._io.read_u2le()
            self.reserved1 = self._io.read_bytes(4)
            self.unnum_cells = self._io.read_u2le()
            self._raw_unnum_text = self._io.read_bytes(4)
            _io__raw_unnum_text = KaitaiStream(BytesIO(self._raw_unnum_text))
            self.unnum_text = Ocd2018.PascalString(_io__raw_unnum_text, self, self._root)
            self.line_style = self._io.read_u2le()
            self.reserved2 = self._io.read_bytes(34)
            self.font_size = self._io.read_u2le()
            self.reserved3 = self._io.read_bytes(8)


    class TStringIndex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pos = self._io.read_u4le()
            self.len = self._io.read_u4le()
            self.rec_type = self._io.read_u4le()
            self.obj_index = self._io.read_u4le()

        @property
        def parameter_string(self):
            if hasattr(self, '_m_parameter_string'):
                return self._m_parameter_string if hasattr(self, '_m_parameter_string') else None

            if self.rec_type > 0:
                _pos = self._io.pos()
                self._io.seek(self.pos)
                self._m_parameter_string = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len), 0, False)).decode(u"ISO8859-1")
                self._io.seek(_pos)

            return self._m_parameter_string if hasattr(self, '_m_parameter_string') else None


    class TPointSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data_size = self._io.read_u2le()
            self.reserved = self._io.read_u2le()
            if self.data_size > 0:
                self._raw_elements = self._io.read_bytes((self.data_size * 8))
                _io__raw_elements = KaitaiStream(BytesIO(self._raw_elements))
                self.elements = Ocd2018.TSymElements(_io__raw_elements, self, self._root)



    @property
    def file_name(self):
        if hasattr(self, '_m_file_name'):
            return self._m_file_name if hasattr(self, '_m_file_name') else None

        _pos = self._io.pos()
        self._io.seek(self.file_header.file_name_pos)
        self._m_file_name = (self._io.read_bytes(self.file_header.file_name_size)).decode(u"ISO8859-1")
        self._io.seek(_pos)
        return self._m_file_name if hasattr(self, '_m_file_name') else None

    @property
    def symbol_index(self):
        if hasattr(self, '_m_symbol_index'):
            return self._m_symbol_index if hasattr(self, '_m_symbol_index') else None

        _pos = self._io.pos()
        self._io.seek(self.file_header.first_symbol_index_block)
        self._m_symbol_index = Ocd2018.TSymbolIndexBlock(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_symbol_index if hasattr(self, '_m_symbol_index') else None

    @property
    def string_index(self):
        if hasattr(self, '_m_string_index'):
            return self._m_string_index if hasattr(self, '_m_string_index') else None

        _pos = self._io.pos()
        self._io.seek(self.file_header.first_string_index_block)
        self._m_string_index = Ocd2018.TStringIndexBlock(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_string_index if hasattr(self, '_m_string_index') else None

    @property
    def object_index(self):
        if hasattr(self, '_m_object_index'):
            return self._m_object_index if hasattr(self, '_m_object_index') else None

        _pos = self._io.pos()
        self._io.seek(self.file_header.first_object_index_block)
        self._m_object_index = Ocd2018.TObjectIndexBlock(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_object_index if hasattr(self, '_m_object_index') else None



