# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_messages.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13test_messages.proto\"\xe9\x02\n\x13\x43omplexProtoMessage\x12\x10\n\x08number32\x18\x01 \x01(\r\x12\x10\n\x08number64\x18\x02 \x01(\x04\x12\x15\n\rlist_number32\x18\x03 \x03(\r\x12\x15\n\rlist_number64\x18\x04 \x03(\x04\x12\x33\n\x08messages\x18\x05 \x03(\x0b\x32!.ComplexProtoMessage.InnerMessage\x12\x31\n\x07\x62uffers\x18\x06 \x03(\x0b\x32 .ComplexProtoMessage.InnerBuffer\x1a-\n\x0cInnerMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0f\n\x07numbers\x18\x02 \x03(\r\x1ai\n\x0bInnerBuffer\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x35\n\x05\x66lags\x18\x02 \x03(\x0b\x32&.ComplexProtoMessage.InnerBuffer.Flags\x1a\x15\n\x05\x46lags\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMPLEXPROTOMESSAGE']._serialized_start=24
  _globals['_COMPLEXPROTOMESSAGE']._serialized_end=385
  _globals['_COMPLEXPROTOMESSAGE_INNERMESSAGE']._serialized_start=233
  _globals['_COMPLEXPROTOMESSAGE_INNERMESSAGE']._serialized_end=278
  _globals['_COMPLEXPROTOMESSAGE_INNERBUFFER']._serialized_start=280
  _globals['_COMPLEXPROTOMESSAGE_INNERBUFFER']._serialized_end=385
  _globals['_COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS']._serialized_start=364
  _globals['_COMPLEXPROTOMESSAGE_INNERBUFFER_FLAGS']._serialized_end=385
# @@protoc_insertion_point(module_scope)
