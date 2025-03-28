# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_datapublisher.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steammessages_datapublisher.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x88\x02\n9CDataPublisher_ClientContentCorruptionReport_Notification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07\x64\x65potid\x18\x02 \x01(\r\x12\x17\n\x0f\x64ownload_source\x18\x03 \x01(\t\x12\x10\n\x08objectid\x18\x04 \x01(\t\x12\x0e\n\x06\x63\x65llid\x18\x05 \x01(\r\x12\x13\n\x0bis_manifest\x18\x06 \x01(\x08\x12\x13\n\x0bobject_size\x18\x07 \x01(\x04\x12\x17\n\x0f\x63orruption_type\x18\x08 \x01(\r\x12\x12\n\nused_https\x18\t \x01(\x08\x12\x19\n\x11oc_proxy_detected\x18\n \x01(\x08\"\xf8\x04\n.CDataPublisher_ClientUpdateAppJob_Notification\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x11\n\tdepot_ids\x18\x02 \x03(\r\x12\x11\n\tapp_state\x18\x03 \x01(\r\x12\x15\n\rjob_app_error\x18\x04 \x01(\r\x12\x15\n\rerror_details\x18\x05 \x01(\t\x12\x14\n\x0cjob_duration\x18\x06 \x01(\r\x12\x1f\n\x17\x66iles_validation_failed\x18\x07 \x01(\r\x12\x1c\n\x14job_bytes_downloaded\x18\x08 \x01(\x04\x12\x18\n\x10job_bytes_staged\x18\t \x01(\x04\x12\x16\n\x0e\x62ytes_comitted\x18\n \x01(\x04\x12\x17\n\x0fstart_app_state\x18\x0b \x01(\r\x12\x18\n\x10stats_machine_id\x18\x0c \x01(\x06\x12\x13\n\x0b\x62ranch_name\x18\r \x01(\t\x12\x1e\n\x16total_bytes_downloaded\x18\x0e \x01(\x04\x12\x1a\n\x12total_bytes_staged\x18\x0f \x01(\x04\x12\x1c\n\x14total_bytes_restored\x18\x10 \x01(\x04\x12\x13\n\x0bis_borrowed\x18\x11 \x01(\x08\x12\x17\n\x0fis_free_weekend\x18\x12 \x01(\x08\x12\x1b\n\x13total_bytes_patched\x18\x14 \x01(\x04\x12\x19\n\x11total_bytes_saved\x18\x15 \x01(\x04\x12\x0f\n\x07\x63\x65ll_id\x18\x16 \x01(\r\x12\x13\n\x0bis_workshop\x18\x17 \x01(\x08\x12\x11\n\tis_shader\x18\x18 \x01(\x08\x12\x1a\n\x12seconds_not_played\x18\x19 \x01(\r\"=\n&CDataPublisher_GetVRDeviceInfo_Request\x12\x13\n\x0bmonth_count\x18\x01 \x01(\r\"\xdd\x01\n\'CDataPublisher_GetVRDeviceInfo_Response\x12?\n\x06\x64\x65vice\x18\x01 \x03(\x0b\x32/.CDataPublisher_GetVRDeviceInfo_Response.Device\x1aq\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x02 \x01(\r\x12\x17\n\x0f\x61ggregation_ref\x18\x03 \x01(\r\x12\r\n\x05total\x18\x04 \x01(\r\x12\x0e\n\x06\x64river\x18\x05 \x01(\t\x12\x14\n\x0c\x64\x65vice_class\x18\x06 \x01(\x05\"b\n:CDataPublisher_SetVRDeviceInfoAggregationReference_Request\x12\x0b\n\x03ref\x18\x01 \x01(\r\x12\x17\n\x0f\x61ggregation_ref\x18\x02 \x01(\r\"M\n;CDataPublisher_SetVRDeviceInfoAggregationReference_Response\x12\x0e\n\x06result\x18\x01 \x01(\r\"\x8c\x01\n&CDataPublisher_AddVRDeviceInfo_Request\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06\x64river\x18\x03 \x01(\t\x12\x17\n\x0f\x63ontroller_type\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x65vice_class\x18\x05 \x01(\x05\"F\n\'CDataPublisher_AddVRDeviceInfo_Response\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x02 \x01(\r\"c\n(CValveHWSurvey_GetSurveySchedule_Request\x12\x17\n\x0fsurveydatetoken\x18\x01 \x01(\t\x12\x1e\n\x16surveydatetokenversion\x18\x02 \x01(\x06\"d\n)CValveHWSurvey_GetSurveySchedule_Response\x12\x17\n\x0fsurveydatetoken\x18\x01 \x01(\r\x12\x1e\n\x16surveydatetokenversion\x18\x02 \x01(\x06\x32\xc2\x04\n\rDataPublisher\x12h\n\x1d\x43lientContentCorruptionReport\x12:.CDataPublisher_ClientContentCorruptionReport_Notification\x1a\x0b.NoResponse\x12X\n\x18\x43lientUpdateAppJobReport\x12/.CDataPublisher_ClientUpdateAppJob_Notification\x1a\x0b.NoResponse\x12\x64\n\x0fGetVRDeviceInfo\x12\'.CDataPublisher_GetVRDeviceInfo_Request\x1a(.CDataPublisher_GetVRDeviceInfo_Response\x12\xa0\x01\n#SetVRDeviceInfoAggregationReference\x12;.CDataPublisher_SetVRDeviceInfoAggregationReference_Request\x1a<.CDataPublisher_SetVRDeviceInfoAggregationReference_Response\x12\x64\n\x0f\x41\x64\x64VRDeviceInfo\x12\'.CDataPublisher_AddVRDeviceInfo_Request\x1a(.CDataPublisher_AddVRDeviceInfo_Response2{\n\rValveHWSurvey\x12j\n\x11GetSurveySchedule\x12).CValveHWSurvey_GetSurveySchedule_Request\x1a*.CValveHWSurvey_GetSurveySchedule_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_datapublisher_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CDATAPUBLISHER_CLIENTCONTENTCORRUPTIONREPORT_NOTIFICATION']._serialized_start=98
  _globals['_CDATAPUBLISHER_CLIENTCONTENTCORRUPTIONREPORT_NOTIFICATION']._serialized_end=362
  _globals['_CDATAPUBLISHER_CLIENTUPDATEAPPJOB_NOTIFICATION']._serialized_start=365
  _globals['_CDATAPUBLISHER_CLIENTUPDATEAPPJOB_NOTIFICATION']._serialized_end=997
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_REQUEST']._serialized_start=999
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_REQUEST']._serialized_end=1060
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_RESPONSE']._serialized_start=1063
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_RESPONSE']._serialized_end=1284
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_RESPONSE_DEVICE']._serialized_start=1171
  _globals['_CDATAPUBLISHER_GETVRDEVICEINFO_RESPONSE_DEVICE']._serialized_end=1284
  _globals['_CDATAPUBLISHER_SETVRDEVICEINFOAGGREGATIONREFERENCE_REQUEST']._serialized_start=1286
  _globals['_CDATAPUBLISHER_SETVRDEVICEINFOAGGREGATIONREFERENCE_REQUEST']._serialized_end=1384
  _globals['_CDATAPUBLISHER_SETVRDEVICEINFOAGGREGATIONREFERENCE_RESPONSE']._serialized_start=1386
  _globals['_CDATAPUBLISHER_SETVRDEVICEINFOAGGREGATIONREFERENCE_RESPONSE']._serialized_end=1463
  _globals['_CDATAPUBLISHER_ADDVRDEVICEINFO_REQUEST']._serialized_start=1466
  _globals['_CDATAPUBLISHER_ADDVRDEVICEINFO_REQUEST']._serialized_end=1606
  _globals['_CDATAPUBLISHER_ADDVRDEVICEINFO_RESPONSE']._serialized_start=1608
  _globals['_CDATAPUBLISHER_ADDVRDEVICEINFO_RESPONSE']._serialized_end=1678
  _globals['_CVALVEHWSURVEY_GETSURVEYSCHEDULE_REQUEST']._serialized_start=1680
  _globals['_CVALVEHWSURVEY_GETSURVEYSCHEDULE_REQUEST']._serialized_end=1779
  _globals['_CVALVEHWSURVEY_GETSURVEYSCHEDULE_RESPONSE']._serialized_start=1781
  _globals['_CVALVEHWSURVEY_GETSURVEYSCHEDULE_RESPONSE']._serialized_end=1881
  _globals['_DATAPUBLISHER']._serialized_start=1884
  _globals['_DATAPUBLISHER']._serialized_end=2462
  _globals['_VALVEHWSURVEY']._serialized_start=2464
  _globals['_VALVEHWSURVEY']._serialized_end=2587
_builder.BuildServices(DESCRIPTOR, 'steammessages_datapublisher_pb2', _globals)
# @@protoc_insertion_point(module_scope)
