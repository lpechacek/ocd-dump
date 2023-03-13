meta:
  id: ocd12
  file-extension: ocd
  endian: le

seq:
  - id: file_header
    type: ocd_file_header

types:
  ocd_file_header:
    seq:
      - id: magic
        contents: [ 0xad, 0x0c ]
      - id: file_type
        type: u1
        enum: e_file_type
      - id: file_status
        type: u1
        doc: Unused
      - id: version
        type: u2
      - id: sub_version
        type: u1
      - id: sub_sub_version
        type: u1
      - id: first_symbol_index_block
        type: u4
      - id: first_object_index_block
        type: u4
      - id: offline_sync_serial
        type: u4
      - id: current_file_version
        type: u4
      - id: reserved1
        size: 8
        doc: internal use
      - id: first_string_index_block
        type: u4
      - id: file_name_pos
        type: u4
      - id: file_name_size
        type: u4
      - id: reserved2
        size: 12
        doc: internal use
      - id: first_mr_index_block
        type: u4

  t_symbol_base:
    seq:
      - id: size
        type: u4
      - id: sym_num
        type: u4
      - id: otp
        type: u1
        enum: e_obj_et_sym_types
      - id: flags
        type: u1
      - id: selected
        type: u1
      - id: status
        type: u1
      - id: drawing_tool
        type: u1
      - id: cs_mode
        type: u1
      - id: cs_objtype
        type: u1
      - id: cs_cdflags
        type: u1
      - id: extent
        type: u4
      - id: file_pos
        type: u4
        doc: internal use
      - id: reserved1
        size: 2
        doc: unused
      - id: n_colors
        type: u2
      - id: colors
        type: u2
        repeat: expr
        repeat-expr: 14
      - id: description
        type: str
        size: 128
        encoding: UTF-16LE
      - id: icon_bits
        size: 484
      - id: symbol_tree_group
        type: u2
        repeat: expr
        repeat-expr: 64

  t_sym_elt:
    seq:
      - id: st_type
        type: u2
        enum: e_symbol_element_type
      - id: st_flags
        type: u2
      - id: st_color
        type: u2
      - id: st_line_width
        type: u2
      - id: st_diameter
        type: u2
      - id: st_n_poly
        type: u2
      - id: reserved1
        size: 4
      - id: st_poly
        type: t_sym_element_poly
        size: st_n_poly * 8

  # aux type for the above repetition
  t_sym_element_poly:
    seq:
      - id: entries
        type: t_d_poly
        repeat: eos

  t_point_symbol:
    seq:
      - id: data_size
        type: u2
      - id: reserved
        type: u2
      - id: elements
        type: t_sym_elements
        size: data_size * 8
        if: data_size > 0

  # aux type for the above repetition, fills the whole
  # substream defined by parent structure
  t_sym_elements:
    seq:
      - id: entries
        type: t_sym_elt
        repeat: eos

  t_line_symbol:
    seq:
      - id: line_color
        type: u2
      - id: line_width
        type: u2
      - id: line_style
        type: u2
      - id: dist_from_start
        type: u2
      - id: dist_to_end
        type: u2
      - id: main_length
        type: u2
      - id: end_length
        type: u2
      - id: main_gap
        type: u2
      - id: sec_gap
        type: u2
      - id: end_gap
        type: u2
      - id: min_sym
        type: u2
      - id: n_prim_sym
        type: u2
      - id: prim_sym_dist
        type: u2
      - id: dbl_mode
        type: u2
      - id: dbl_flags
        type: u2
      - id: dbl_fill_color
        type: u2
      - id: dbl_left_color
        type: u2
      - id: dbl_right_color
        type: u2
      - id: dbl_width
        type: u2
      - id: dbl_left_width
        type: u2
      - id: dbl_right_width
        type: u2
      - id: dbl_length
        type: u2
      - id: dbl_gap
        type: u2
      - id: reserved1
        size: 6
      - id: dec_mode
        type: u2
      - id: dec_symbol_size
        type: u2
      - id: dec_symbol_distance
        type: u1
      - id: dec_symbol_width
        type: u1
      - id: fr_color
        type: u2
      - id: fr_width
        type: u2
      - id: fr_style
        type: u2
      - id: prim_dsize
        type: u2
      - id: sec_dsize
        type: u2
      - id: corner_dsize
        type: u2
      - id: start_dsize
        type: u2
      - id: end_dsize
        type: u2
      - id: use_symbol_flags
        type: u1
      - id: reserved
        type: u1
      - id: prim_elements
        type: t_sym_elements
        size: prim_dsize * 8
        if: prim_dsize > 0
      - id: sec_elements
        type: t_sym_elements
        size: sec_dsize * 8
        if: sec_dsize > 0
      - id: corner_elements
        type: t_sym_elements
        size: corner_dsize * 8
        if: corner_dsize > 0
      - id: start_elements
        type: t_sym_elements
        size: start_dsize * 8
        if: start_dsize > 0
      - id: end_elements
        type: t_sym_elements
        size: end_dsize * 8
        if: end_dsize > 0

  t_area_symbol:
    seq:
      - id: border_sym
        type: u4
      - id: fill_color
        type: u2
      - id: hatch_mode
        type: u2
        enum: e_area_hatch_mode
      - id: hatch_color
        type: u2
      - id: hatch_line_width
        type: u2
      - id: hatch_dist
        type: u2
      - id: hatch_angle1
        type: u2
      - id: hatch_angle2
        type: u2
      - id: fill_on
        type: u1
      - id: border_on
        type: u1
      - id: struct_mode
        type: u1
        enum: e_area_struct_mode
      - id: struct_draw
        type: u1
        enum: e_struct_drawing_mode
      - id: struct_width
        type: u2
      - id: struct_height
        type: u2
      - id: struct_angle
        type: u2
      - id: struct_irregular_var_x
        type: u1
      - id: struct_irregular_var_y
        type: u1
      - id: struct_irregular_min_dist
        type: u2
      - id: reserved1
        size: 2
      - id: data_size
        type: u2
      - id: elements
        type: t_sym_elements
        size: data_size * 8
        if: data_size > 0

  t_text_symbol:
    seq:
      - id: font_name
        type: pascal_string
        size: 32
      - id: font_color
        type: u2
      - id: font_size
        type: u2
      - id: weight
        type: u2
      - id: italic
        type: u1
      - id: reserved1
        size: 1
      - id: char_space
        type: u2
      - id: word_space
        type: u2
      - id: alignment
        type: u2
      - id: line_space
        type: u2
      - id: para_space
        type: u2
      - id: indent_first
        type: u2
      - id: indent_other
        type: u2
      - id: n_tabs
        type: u2
      - id: tabs
        type: u4
        repeat: expr
        repeat-expr: 32
      - id: lbon
        type: u2
        doc: treat as boolean
      - id: lbcolor
        type: u2
      - id: lbwidth
        type: u2
      - id: lbdist
        type: u2
      - id: reserved2
        size: 2
      - id: fr_mode
        type: u1
      - id: fr_line_style
        type: u1
      - id: point_sym_on
        type: u1
      - id: point_sym_number
        type: u4
      - id: reserved3
        size: 19
      - id: fr_left
        type: u2
      - id: fr_bottom
        type: u2
      - id: fr_right
        type: u2
      - id: fr_top
        type: u2
      - id: fr_color
        type: u2
      - id: fr_width
        type: u2
      - id: reserved4
        size: 2
      - id: reserved5
        size: 2
      - id: fr_of_x
        type: u2
      - id: fr_of_y
        type: u2

  t_line_text_symbol:
    seq:
      - id: font_name
        type: pascal_string
        size: 32
      - id: font_color
        type: u2
      - id: font_size
        type: u2
      - id: weight
        type: u2
      - id: italic
        type: u1
      - id: reserved1
        size: 1
      - id: char_space
        type: u2
      - id: word_space
        type: u2
      - id: alignment
        type: u2
      - id: fr_mode
        type: u1
      - id: fr_line_style
        type: u1
      - id: reserved2
        size: 32
      - id: fr_color
        type: u2
      - id: fr_width
        type: u2
      - id: reserved3
        size: 4
      - id: fr_of_x
        type: u2
      - id: fr_of_y
        type: u2

  t_rectangle_symbol:
    seq:
      - id: line_color
        type: u2
      - id: line_width
        type: u2
      - id: radius
        type: u2
      - id: grid_flags
        type: u2
      - id: cell_width
        type: u2
      - id: cell_height
        type: u2
      - id: reserved1
        size: 4
      - id: unnum_cells
        type: u2
      - id: unnum_text
        type: pascal_string
        size: 4
      - id: line_style
        type: u2
      - id: reserved2
        size: 34
      - id: font_size
        type: u2
      - id: reserved3
        size: 8

  t_symbol:
    seq:
      - id: base
        type: t_symbol_base
      - id: type_specific
        type:
          switch-on: base.otp
          cases:
            e_obj_et_sym_types::point: t_point_symbol
            e_obj_et_sym_types::line: t_line_symbol
            e_obj_et_sym_types::area: t_area_symbol
            e_obj_et_sym_types::text: t_text_symbol
            e_obj_et_sym_types::line_text: t_line_text_symbol
            e_obj_et_sym_types::rectangle: t_rectangle_symbol

  t_symbol_pos:
    seq:
      - id: pos
        type: u4
    instances:
      symbol:
        type: t_symbol
        pos: pos
        io: _root._io
        if: pos > 0

  t_symbol_index_block:
    seq:
      - id: next_index_block
        type: u4
      - id: symbol_position
        type: t_symbol_pos
        repeat: expr
        repeat-expr: 256
    instances:
      next:
        type: t_symbol_index_block
        pos: next_index_block
        io: _root._io
        if: next_index_block != 0

  t_string_index:
    seq:
      - id: pos
        type: u4
      - id: len
        type: u4
      - id: rec_type
        type: u4
      - id: obj_index
        type: u4
    instances:
      parameter_string:
        type: strz
        pos: pos
        size: len
        encoding: ISO8859-1
        if: rec_type > 0

  t_string_index_block:
    seq:
      - id: next_index_block
        type: u4
      - id: string_table
        type: t_string_index
        repeat: expr
        repeat-expr: 256
    instances:
      next:
        type: t_string_index_block
        pos: next_index_block
        io: _root._io
        if: next_index_block != 0

  t_object_index:
    seq:
      - id: rc
        type: t_d_poly
        repeat: expr
        repeat-expr: 2
      - id: pos
        type: u4
      - id: len
        type: u4
      - id: sym
        type: s4
      - id: obj_type
        type: u1
        enum: e_obj_et_sym_types
      - id: encrypted_mode
        type: u1
      - id: status
        type: u1
        enum: e_object_status
      - id: view_type
        type: u1
        enum: e_object_view_mode
      - id: color
        type: s2
      - id: group
        type: s2
      - id: imp_layer
        type: s2
      - id: reserved1
        size: 2
    instances:
      object:
        type: t_element
        pos: pos
        size: len
        doc: I'm not sure if the entry:element is 1:1 relationship.
             Verify that there cannot be more TElement structures packed in
             the space reserved by t_object_index.len.

  t_object_index_block:
    seq:
      - id: next_index_block
        type: u4
      - id: object_table
        type: t_object_index
        repeat: expr
        repeat-expr: 256
    instances:
      next:
        type: t_object_index_block
        pos: next_index_block
        io: _root._io
        if: next_index_block != 0

  t_element:
    seq:
      - id: sym
        type: s4
      - id: otp
        type: u1
        enum: e_obj_et_sym_types
      - id: reserved1
        size: 1
      - id: ang
        type: s2
      - id: color
        type: u4
      - id: line_width
        type: s2
      - id: diam_flags
        type: s2
      - id: server_object_id
        type: u4
      - id: height
        type: u4
      - id: creation_date
        type: f8
      - id: multirepresentation_id
        type: u4
      - id: modification_date
        type: f8
      - id: n_item
        type: u4
      - id: n_text
        type: u2
      - id: n_object_string
        type: u2
      - id: n_database_string
        type: u2
      - id: object_string_type
        type: u1
        enum: e_object_string_type
      - id: reserved2
        size: 1
      - id: poly
        type: t_d_poly
        repeat: expr
        repeat-expr: n_item
        if: n_item != 0 and otp.to_i != 1
      - id: center
        type: t_d_poly
        if: otp.to_i == 1
      - id: cut_angles
        type: point_symbol_cut_angle
        repeat: expr
        repeat-expr: n_item - 1
        if: n_item > 1 and otp.to_i == 1
      - id: text
        type: str
        encoding: UTF-16LE
        size: n_text*8
        if: n_text != 0

  t_d_poly:
    seq:
      - id: x_value
        type: s4
      - id: y_value
        type: s4
    instances:
      flags:
        value: (x_value & 0x0F) | ((y_value & 0x0F) << 4)
      x_coord:
        value: x_value / 256
      y_coord:
        value: y_value / 256

  point_symbol_cut_angle:
    doc: Cut angles in tenths of degrees.
    seq:
      - id: start_deg
        type: s4
      - id: end_deg
        type: s4

  pascal_string:
    seq:
      - id: len
        type: u1
      - id: data
        size: len
        type: str
        encoding: ISO8859-1
    instances:
      value:
        value: data

enums:
  e_file_type:
    0: normal_map
    1: course_setting_project
    8: server_stored_file

  e_symbol_element_type:
    1: line
    2: area
    3: circle
    4: dot

  e_obj_et_sym_types:
    1: point
    2: line
    3: area
    4: text
    6: line_text
    7: rectangle

  e_area_hatch_mode:
    0: none
    1: single_hatch
    2: cross_hatch

  e_area_struct_mode:
    0: none
    1: aliged_rows
    2: shifted_rows

  e_struct_drawing_mode:
    0: clip
    1: completely_inside
    2: center_inside
    3: partially_inside

  e_object_status:
    0: deleted_no_undo
    1: normal
    2: hidden
    3: deleted_for_undo

  e_object_view_mode:
    0: normal
    1: course_setting_object
    2: modified_preview_onject
    3: unmodified_preview_object
    4: temporary_object

  e_object_string_type:
    0: none
    1: course_setting_object
    2: course_setting_preview_object
    3: course_setting_layout_object
    4: course_setting_thematic_object

instances:
  file_name:
    type: str
    pos: file_header.file_name_pos
    size: file_header.file_name_size
    encoding: ISO8859-1

  symbol_index:
    type: t_symbol_index_block
    pos: file_header.first_symbol_index_block

  string_index:
    type: t_string_index_block
    pos: file_header.first_string_index_block

  object_index:
    type: t_object_index_block
    pos: file_header.first_object_index_block
