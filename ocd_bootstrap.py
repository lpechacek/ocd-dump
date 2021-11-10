# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class OcdBootstrap(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(2)
        if not self.magic == b"\xAD\x0C":
            raise kaitaistruct.ValidationNotEqualError(b"\xAD\x0C", self.magic, self._io, u"/seq/0")
        self.file_type = self._io.read_u1()
        self.file_status = self._io.read_u1()
        self.version = self._io.read_u2le()
        self.sub_version = self._io.read_u1()
        self.sub_sub_version = self._io.read_u1()



