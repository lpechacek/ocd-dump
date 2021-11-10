meta:
  id: ocd_bootstrap
  file-extension: ocd
  endian: le

seq:
  - id: magic
    contents: [ 0xad, 0x0c ]
  - id: file_type
    type: u1
  - id: file_status
    type: u1
    doc: Unused
  - id: version
    type: u2
  - id: sub_version
    type: u1
  - id: sub_sub_version
    type: u1
