# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rexample.proto\"n\n\x06person\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x17\n\x06gender\x18\x04 \x01(\x0e\x32\x07.gender\x12\x19\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32\x08.address\",\n\x07\x61\x64\x64ress\x12\x10\n\x08postcode\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t*&\n\x06gender\x12\x06\n\x02nb\x10\x00\x12\x08\n\x04male\x10\x01\x12\n\n\x06\x66\x65male\x10\x02\x62\x06proto3')
)

_GENDER = _descriptor.EnumDescriptor(
  name='gender',
  full_name='gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='nb', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='male', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='female', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=175,
  serialized_end=213,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
nb = 0
male = 1
female = 2



_PERSON = _descriptor.Descriptor(
  name='person',
  full_name='person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstName', full_name='person.firstName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='person.lastName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='person.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='person.gender', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='person.address', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=127,
)


_ADDRESS = _descriptor.Descriptor(
  name='address',
  full_name='address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='postcode', full_name='address.postcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='address.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=173,
)

_PERSON.fields_by_name['gender'].enum_type = _GENDER
_PERSON.fields_by_name['address'].message_type = _ADDRESS
DESCRIPTOR.message_types_by_name['person'] = _PERSON
DESCRIPTOR.message_types_by_name['address'] = _ADDRESS
DESCRIPTOR.enum_types_by_name['gender'] = _GENDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

person = _reflection.GeneratedProtocolMessageType('person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:person)
  })
_sym_db.RegisterMessage(person)

address = _reflection.GeneratedProtocolMessageType('address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:address)
  })
_sym_db.RegisterMessage(address)


# @@protoc_insertion_point(module_scope)
