# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: umbra.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='umbra.proto',
  package='umbra',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bumbra.proto\x12\x05umbra\x1a\x1fgoogle/protobuf/timestamp.proto\"U\n\x06\x43onfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08scenario\x18\x02 \x01(\x0c\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"S\n\x06Report\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x0c\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"g\n\x06\x44\x65ploy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08workflow\x18\x02 \x01(\t\x12\x10\n\x08scenario\x18\x03 \x01(\x0c\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"k\n\x05\x42uilt\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ok\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\x0c\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2-\n\x06\x42roker\x12#\n\x03Run\x12\r.umbra.Config\x1a\r.umbra.Report2.\n\x08Scenario\x12\"\n\x03Run\x12\r.umbra.Deploy\x1a\x0c.umbra.Builtb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='umbra.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='umbra.Config.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenario', full_name='umbra.Config.scenario', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='umbra.Config.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=55,
  serialized_end=140,
)


_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='umbra.Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='umbra.Report.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='umbra.Report.status', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='umbra.Report.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=142,
  serialized_end=225,
)


_DEPLOY = _descriptor.Descriptor(
  name='Deploy',
  full_name='umbra.Deploy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='umbra.Deploy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='umbra.Deploy.workflow', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenario', full_name='umbra.Deploy.scenario', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='umbra.Deploy.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=227,
  serialized_end=330,
)


_BUILT = _descriptor.Descriptor(
  name='Built',
  full_name='umbra.Built',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='umbra.Built.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ok', full_name='umbra.Built.ok', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='umbra.Built.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='umbra.Built.info', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='umbra.Built.timestamp', index=4,
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
  serialized_start=332,
  serialized_end=439,
)

_CONFIG.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REPORT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Report'] = _REPORT
DESCRIPTOR.message_types_by_name['Deploy'] = _DEPLOY
DESCRIPTOR.message_types_by_name['Built'] = _BUILT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'umbra_pb2'
  # @@protoc_insertion_point(class_scope:umbra.Config)
  })
_sym_db.RegisterMessage(Config)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'umbra_pb2'
  # @@protoc_insertion_point(class_scope:umbra.Report)
  })
_sym_db.RegisterMessage(Report)

Deploy = _reflection.GeneratedProtocolMessageType('Deploy', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOY,
  '__module__' : 'umbra_pb2'
  # @@protoc_insertion_point(class_scope:umbra.Deploy)
  })
_sym_db.RegisterMessage(Deploy)

Built = _reflection.GeneratedProtocolMessageType('Built', (_message.Message,), {
  'DESCRIPTOR' : _BUILT,
  '__module__' : 'umbra_pb2'
  # @@protoc_insertion_point(class_scope:umbra.Built)
  })
_sym_db.RegisterMessage(Built)



_BROKER = _descriptor.ServiceDescriptor(
  name='Broker',
  full_name='umbra.Broker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=441,
  serialized_end=486,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='umbra.Broker.Run',
    index=0,
    containing_service=None,
    input_type=_CONFIG,
    output_type=_REPORT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROKER)

DESCRIPTOR.services_by_name['Broker'] = _BROKER


_SCENARIO = _descriptor.ServiceDescriptor(
  name='Scenario',
  full_name='umbra.Scenario',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=488,
  serialized_end=534,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='umbra.Scenario.Run',
    index=0,
    containing_service=None,
    input_type=_DEPLOY,
    output_type=_BUILT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCENARIO)

DESCRIPTOR.services_by_name['Scenario'] = _SCENARIO

# @@protoc_insertion_point(module_scope)