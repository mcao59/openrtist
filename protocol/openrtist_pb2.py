# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openrtist.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openrtist.proto',
  package='openrtist',
  syntax='proto3',
  serialized_pb=_b('\n\x0fopenrtist.proto\x12\topenrtist\"\xc7\x02\n\x0c\x45ngineFields\x12\r\n\x05style\x18\x01 \x01(\t\x12:\n\nstyle_list\x18\x02 \x03(\x0b\x32&.openrtist.EngineFields.StyleListEntry\x12\x37\n\x0bstyle_image\x18\x03 \x01(\x0b\x32\".openrtist.EngineFields.BytesValue\x12\x36\n\ntimestamps\x18\x04 \x01(\x0b\x32\".openrtist.EngineFields.Timestamps\x1a\x1b\n\nBytesValue\x12\r\n\x05value\x18\x01 \x01(\x0c\x1a,\n\nTimestamps\x12\x10\n\x08received\x18\x01 \x01(\x01\x12\x0c\n\x04sent\x18\x02 \x01(\x01\x1a\x30\n\x0eStyleListEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1e\n\x14\x65\x64u.cmu.cs.openrtistB\x06Protosb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENGINEFIELDS_BYTESVALUE = _descriptor.Descriptor(
  name='BytesValue',
  full_name='openrtist.EngineFields.BytesValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='openrtist.EngineFields.BytesValue.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=262,
)

_ENGINEFIELDS_TIMESTAMPS = _descriptor.Descriptor(
  name='Timestamps',
  full_name='openrtist.EngineFields.Timestamps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='received', full_name='openrtist.EngineFields.Timestamps.received', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sent', full_name='openrtist.EngineFields.Timestamps.sent', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=308,
)

_ENGINEFIELDS_STYLELISTENTRY = _descriptor.Descriptor(
  name='StyleListEntry',
  full_name='openrtist.EngineFields.StyleListEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='openrtist.EngineFields.StyleListEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='openrtist.EngineFields.StyleListEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=358,
)

_ENGINEFIELDS = _descriptor.Descriptor(
  name='EngineFields',
  full_name='openrtist.EngineFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='style', full_name='openrtist.EngineFields.style', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='style_list', full_name='openrtist.EngineFields.style_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='style_image', full_name='openrtist.EngineFields.style_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamps', full_name='openrtist.EngineFields.timestamps', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENGINEFIELDS_BYTESVALUE, _ENGINEFIELDS_TIMESTAMPS, _ENGINEFIELDS_STYLELISTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=358,
)

_ENGINEFIELDS_BYTESVALUE.containing_type = _ENGINEFIELDS
_ENGINEFIELDS_TIMESTAMPS.containing_type = _ENGINEFIELDS
_ENGINEFIELDS_STYLELISTENTRY.containing_type = _ENGINEFIELDS
_ENGINEFIELDS.fields_by_name['style_list'].message_type = _ENGINEFIELDS_STYLELISTENTRY
_ENGINEFIELDS.fields_by_name['style_image'].message_type = _ENGINEFIELDS_BYTESVALUE
_ENGINEFIELDS.fields_by_name['timestamps'].message_type = _ENGINEFIELDS_TIMESTAMPS
DESCRIPTOR.message_types_by_name['EngineFields'] = _ENGINEFIELDS

EngineFields = _reflection.GeneratedProtocolMessageType('EngineFields', (_message.Message,), dict(

  BytesValue = _reflection.GeneratedProtocolMessageType('BytesValue', (_message.Message,), dict(
    DESCRIPTOR = _ENGINEFIELDS_BYTESVALUE,
    __module__ = 'openrtist_pb2'
    # @@protoc_insertion_point(class_scope:openrtist.EngineFields.BytesValue)
    ))
  ,

  Timestamps = _reflection.GeneratedProtocolMessageType('Timestamps', (_message.Message,), dict(
    DESCRIPTOR = _ENGINEFIELDS_TIMESTAMPS,
    __module__ = 'openrtist_pb2'
    # @@protoc_insertion_point(class_scope:openrtist.EngineFields.Timestamps)
    ))
  ,

  StyleListEntry = _reflection.GeneratedProtocolMessageType('StyleListEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENGINEFIELDS_STYLELISTENTRY,
    __module__ = 'openrtist_pb2'
    # @@protoc_insertion_point(class_scope:openrtist.EngineFields.StyleListEntry)
    ))
  ,
  DESCRIPTOR = _ENGINEFIELDS,
  __module__ = 'openrtist_pb2'
  # @@protoc_insertion_point(class_scope:openrtist.EngineFields)
  ))
_sym_db.RegisterMessage(EngineFields)
_sym_db.RegisterMessage(EngineFields.BytesValue)
_sym_db.RegisterMessage(EngineFields.Timestamps)
_sym_db.RegisterMessage(EngineFields.StyleListEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024edu.cmu.cs.openrtistB\006Protos'))
_ENGINEFIELDS_STYLELISTENTRY.has_options = True
_ENGINEFIELDS_STYLELISTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
