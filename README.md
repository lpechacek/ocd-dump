# A helper tool to dump .ocd format in text form

`ocd-dump` is a debugging tool leveraging [Kaitai
Struct](https://github.com/kaitai-io/kaitai_struct) for description of the .ocd
binary format, which is a common data representation of orienteering
maps.

`ocad*.ksy` are the YAML format description. `ocd_dump.py` is the
actual tool. Other `ocd*` are generated files, notably the PDF diagram.
Currently, v10, v12 and v2018 formats are implemented.

```
usage: ocd_dump.py [-h] [--start SECTION_NAME] [--skip SECTION_NAME] [--print-empty] file

Dump ocd file contents in text format.

positional arguments:
  file                  .ocd file to be processed

optional arguments:
  -h, --help            show this help message and exit
  --start SECTION_NAME  start with at specified file section,
                        e.g. 'object_index' or 'string_index'
  --skip SECTION_NAME   skip a file section, e.g. 'object_index' or
                        'string_index'; the option can be specified multiple times
  --print-empty         print empty index positions
```

