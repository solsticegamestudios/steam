# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_siteserverui.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steammessages_siteserverui.proto\x1a\x18steammessages_base.proto\"s\n\x1aSiteServerUI_Login_Request\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x16\n\x0esteamguardcode\x18\x03 \x01(\t\x12\x19\n\x11remember_password\x18\x04 \x01(\x08\"I\n\x1bSiteServerUI_Login_Response\x12\x13\n\x0blogon_state\x18\x01 \x01(\x05\x12\x15\n\rlogon_eresult\x18\x02 \x01(\x05\"\"\n SiteServerUI_LoginStatus_Request\"}\n!SiteServerUI_LoginStatus_Response\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x1a\n\x12\x63\x61\x63hed_credentials\x18\x02 \x01(\x08\x12\x13\n\x0blogon_state\x18\x03 \x01(\x05\x12\x15\n\rlogon_eresult\x18\x04 \x01(\x05\"\"\n SiteServerUI_CancelLogin_Request\"O\n!SiteServerUI_CancelLogin_Response\x12\x13\n\x0blogon_state\x18\x01 \x01(\x05\x12\x15\n\rlogon_eresult\x18\x02 \x01(\x05\"\x1d\n\x1bSiteServerUI_Logout_Request\"K\n\x1cSiteServerUI_Logout_Response\x12\x13\n\x0blogon_state\x18\x01 \x01(\x05\x12\x16\n\x0elogout_eresult\x18\x02 \x01(\x05\",\n\x19SiteServerUI_Quit_Request\x12\x0f\n\x07restart\x18\x01 \x01(\x08\"\x1c\n\x1aSiteServerUI_Quit_Response\"\x1d\n\x1bSiteServerUI_Status_Request\"\x89\x01\n\x1cSiteServerUI_Status_Response\x12\x13\n\x0blogon_state\x18\x01 \x01(\x05\x12\x15\n\rlogon_eresult\x18\x02 \x01(\x05\x12\x11\n\tconnected\x18\x03 \x01(\x08\x12\x15\n\rcache_enabled\x18\x04 \x01(\x08\x12\x13\n\x0b\x61\x63\x63t_status\x18\x05 \x01(\x05\"\"\n SiteServerUI_GetLanguage_Request\"5\n!SiteServerUI_GetLanguage_Response\x12\x10\n\x08language\x18\x01 \x01(\t\"4\n SiteServerUI_SetLanguage_Request\x12\x10\n\x08language\x18\x01 \x01(\t\"#\n!SiteServerUI_SetLanguage_Response\"#\n!SiteServerUI_ClientStatus_Request\"\xb6\x03\n\"SiteServerUI_ClientStatus_Response\x12?\n\x07\x63lients\x18\x04 \x03(\x0b\x32..SiteServerUI_ClientStatus_Response.ClientInfo\x12=\n\x08payments\x18\x05 \x03(\x0b\x32+.SiteServerUI_ClientStatus_Response.Payment\x1aR\n\nClientInfo\x12\n\n\x02ip\x18\x01 \x01(\r\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x11\n\tconnected\x18\x03 \x01(\x08\x12\x13\n\x0binstance_id\x18\x04 \x01(\x04\x1a\xbb\x01\n\x07Payment\x12\x0f\n\x07transid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\x12\x14\n\x0ctime_created\x18\x04 \x01(\x05\x12\x17\n\x0fpurchase_status\x18\x05 \x01(\x05\x12\x10\n\x08hostname\x18\x06 \x01(\t\x12\x14\n\x0cpersona_name\x18\x07 \x01(\t\x12\x13\n\x0bprofile_url\x18\x08 \x01(\t\x12\x12\n\navatar_url\x18\t \x01(\t\")\n\'SiteServerUI_ContentCacheStatus_Request\"\x8b\x02\n(SiteServerUI_ContentCacheStatus_Response\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x16\n\x0e\x63\x61\x63he_location\x18\x03 \x01(\t\x12\x13\n\x0bmax_size_gb\x18\x04 \x01(\r\x12\x13\n\x0bp2p_enabled\x18\x05 \x01(\x08\x12\x1b\n\x13\x65xplicit_ip_address\x18\t \x01(\t\x12\x18\n\x10\x65xternal_process\x18\n \x01(\x08\x12\x17\n\x0f\x63urrent_size_gb\x18\x06 \x01(\r\x12\x12\n\ncurrent_bw\x18\x07 \x01(\x04\x12\x1a\n\x12total_bytes_served\x18\x08 \x01(\x04\"\xc1\x01\n\'SiteServerUI_ContentCacheConfig_Request\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x16\n\x0e\x63\x61\x63he_location\x18\x03 \x01(\t\x12\x13\n\x0bmax_size_gb\x18\x04 \x01(\r\x12\x13\n\x0bp2p_enabled\x18\x05 \x01(\x08\x12\x18\n\x10\x65xternal_process\x18\x06 \x01(\x08\x12\x1b\n\x13\x65xplicit_ip_address\x18\x07 \x01(\t\"*\n(SiteServerUI_ContentCacheConfig_ResponseB\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_siteserverui_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_SITESERVERUI_LOGIN_REQUEST']._serialized_start=62
  _globals['_SITESERVERUI_LOGIN_REQUEST']._serialized_end=177
  _globals['_SITESERVERUI_LOGIN_RESPONSE']._serialized_start=179
  _globals['_SITESERVERUI_LOGIN_RESPONSE']._serialized_end=252
  _globals['_SITESERVERUI_LOGINSTATUS_REQUEST']._serialized_start=254
  _globals['_SITESERVERUI_LOGINSTATUS_REQUEST']._serialized_end=288
  _globals['_SITESERVERUI_LOGINSTATUS_RESPONSE']._serialized_start=290
  _globals['_SITESERVERUI_LOGINSTATUS_RESPONSE']._serialized_end=415
  _globals['_SITESERVERUI_CANCELLOGIN_REQUEST']._serialized_start=417
  _globals['_SITESERVERUI_CANCELLOGIN_REQUEST']._serialized_end=451
  _globals['_SITESERVERUI_CANCELLOGIN_RESPONSE']._serialized_start=453
  _globals['_SITESERVERUI_CANCELLOGIN_RESPONSE']._serialized_end=532
  _globals['_SITESERVERUI_LOGOUT_REQUEST']._serialized_start=534
  _globals['_SITESERVERUI_LOGOUT_REQUEST']._serialized_end=563
  _globals['_SITESERVERUI_LOGOUT_RESPONSE']._serialized_start=565
  _globals['_SITESERVERUI_LOGOUT_RESPONSE']._serialized_end=640
  _globals['_SITESERVERUI_QUIT_REQUEST']._serialized_start=642
  _globals['_SITESERVERUI_QUIT_REQUEST']._serialized_end=686
  _globals['_SITESERVERUI_QUIT_RESPONSE']._serialized_start=688
  _globals['_SITESERVERUI_QUIT_RESPONSE']._serialized_end=716
  _globals['_SITESERVERUI_STATUS_REQUEST']._serialized_start=718
  _globals['_SITESERVERUI_STATUS_REQUEST']._serialized_end=747
  _globals['_SITESERVERUI_STATUS_RESPONSE']._serialized_start=750
  _globals['_SITESERVERUI_STATUS_RESPONSE']._serialized_end=887
  _globals['_SITESERVERUI_GETLANGUAGE_REQUEST']._serialized_start=889
  _globals['_SITESERVERUI_GETLANGUAGE_REQUEST']._serialized_end=923
  _globals['_SITESERVERUI_GETLANGUAGE_RESPONSE']._serialized_start=925
  _globals['_SITESERVERUI_GETLANGUAGE_RESPONSE']._serialized_end=978
  _globals['_SITESERVERUI_SETLANGUAGE_REQUEST']._serialized_start=980
  _globals['_SITESERVERUI_SETLANGUAGE_REQUEST']._serialized_end=1032
  _globals['_SITESERVERUI_SETLANGUAGE_RESPONSE']._serialized_start=1034
  _globals['_SITESERVERUI_SETLANGUAGE_RESPONSE']._serialized_end=1069
  _globals['_SITESERVERUI_CLIENTSTATUS_REQUEST']._serialized_start=1071
  _globals['_SITESERVERUI_CLIENTSTATUS_REQUEST']._serialized_end=1106
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE']._serialized_start=1109
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE']._serialized_end=1547
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE_CLIENTINFO']._serialized_start=1275
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE_CLIENTINFO']._serialized_end=1357
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE_PAYMENT']._serialized_start=1360
  _globals['_SITESERVERUI_CLIENTSTATUS_RESPONSE_PAYMENT']._serialized_end=1547
  _globals['_SITESERVERUI_CONTENTCACHESTATUS_REQUEST']._serialized_start=1549
  _globals['_SITESERVERUI_CONTENTCACHESTATUS_REQUEST']._serialized_end=1590
  _globals['_SITESERVERUI_CONTENTCACHESTATUS_RESPONSE']._serialized_start=1593
  _globals['_SITESERVERUI_CONTENTCACHESTATUS_RESPONSE']._serialized_end=1860
  _globals['_SITESERVERUI_CONTENTCACHECONFIG_REQUEST']._serialized_start=1863
  _globals['_SITESERVERUI_CONTENTCACHECONFIG_REQUEST']._serialized_end=2056
  _globals['_SITESERVERUI_CONTENTCACHECONFIG_RESPONSE']._serialized_start=2058
  _globals['_SITESERVERUI_CONTENTCACHECONFIG_RESPONSE']._serialized_end=2100
# @@protoc_insertion_point(module_scope)
