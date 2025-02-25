# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_inventory.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsteammessages_inventory.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"A\n\x1f\x43Inventory_GetInventory_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\"\x86\x01\n\x13\x43Inventory_Response\x12\x0c\n\x04\x65tag\x18\x01 \x01(\t\x12\x16\n\x0eremoveditemids\x18\x02 \x03(\x04\x12\x11\n\titem_json\x18\x03 \x01(\t\x12\x14\n\x0citemdef_json\x18\x04 \x01(\t\x12\x0e\n\x06ticket\x18\x05 \x01(\x0c\x12\x10\n\x08replayed\x18\x06 \x01(\x08\"\x8e\x01\n\x1f\x43Inventory_ExchangeItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x17\n\x0fmaterialsitemid\x18\x03 \x03(\x04\x12\x19\n\x11materialsquantity\x18\x04 \x03(\r\x12\x17\n\x0foutputitemdefid\x18\x05 \x01(\x04\"O\n-CInventory_GetEligiblePromoItemDefIDs_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\"D\n.CInventory_GetEligiblePromoItemDefIDs_Response\x12\x12\n\nitemdefids\x18\x01 \x03(\x04\"\xd6\x01\n\x1a\x43Inventory_AddItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x03(\x04\x12\x15\n\ritempropsjson\x18\x03 \x03(\t\x12\x14\n\x0citemquantity\x18\t \x03(\r\x12\x0f\n\x07steamid\x18\x04 \x01(\x04\x12\x0e\n\x06notify\x18\x05 \x01(\x08\x12\x11\n\trequestid\x18\x06 \x01(\x04\x12\x19\n\x11trade_restriction\x18\x07 \x01(\x08\x12\x1a\n\x0bis_purchase\x18\x08 \x01(\x08:\x05\x66\x61lse\"\xe5\x02\n\x1e\x43Inventory_ModifyItems_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\x12\x43\n\x07updates\x18\x03 \x03(\x0b\x32\x32.CInventory_ModifyItems_Request.ItemPropertyUpdate\x12\x11\n\ttimestamp\x18\x04 \x01(\r\x1a\xca\x01\n\x12ItemPropertyUpdate\x12\x0e\n\x06itemid\x18\x01 \x01(\x04\x12\x17\n\x0fremove_property\x18\x02 \x01(\x08\x12\x15\n\rproperty_name\x18\x03 \x01(\t\x12\x1b\n\x13property_value_bool\x18\x04 \x01(\x08\x12\x1a\n\x12property_value_int\x18\x05 \x01(\x03\x12\x1d\n\x15property_value_string\x18\x06 \x01(\t\x12\x1c\n\x14property_value_float\x18\x07 \x01(\x02\"F\n\"CInventory_ConsumePlaytime_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x01(\x04\"\x88\x01\n\x1e\x43Inventory_ConsumeItem_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0e\n\x06itemid\x18\x02 \x01(\x04\x12\x10\n\x08quantity\x18\x03 \x01(\r\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0f\n\x07steamid\x18\x05 \x01(\x04\x12\x11\n\trequestid\x18\x06 \x01(\x04\"W\n!CInventory_DevSetNextDrop_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\titemdefid\x18\x02 \x01(\x04\x12\x10\n\x08\x64roptime\x18\x03 \x01(\t\"e\n!CInventory_SplitItemStack_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0e\n\x06itemid\x18\x02 \x01(\x04\x12\x10\n\x08quantity\x18\x03 \x01(\r\x12\x0f\n\x07steamid\x18\x05 \x01(\x04\"\x80\x01\n$CInventory_CombineItemStacks_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\nfromitemid\x18\x02 \x01(\x04\x12\x12\n\ndestitemid\x18\x03 \x01(\x04\x12\x10\n\x08quantity\x18\x04 \x01(\r\x12\x0f\n\x07steamid\x18\x07 \x01(\x06\"2\n!CInventory_GetItemDefMeta_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"F\n\"CInventory_GetItemDefMeta_Response\x12\x10\n\x08modified\x18\x01 \x01(\r\x12\x0e\n\x06\x64igest\x18\x02 \x01(\t\"(\n&CInventory_GetUserPurchaseInfo_Request\"<\n\'CInventory_GetUserPurchaseInfo_Response\x12\x11\n\tecurrency\x18\x01 \x01(\x05\"\xb2\x01\n\x1f\x43Inventory_PurchaseInit_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08language\x18\x02 \x01(\x05\x12=\n\nline_items\x18\x03 \x03(\x0b\x32).CInventory_PurchaseInit_Request.LineItem\x1a/\n\x08LineItem\x12\x11\n\titemdefid\x18\x01 \x01(\x04\x12\x10\n\x08quantity\x18\x02 \x01(\r\"D\n CInventory_PurchaseInit_Response\x12\x0f\n\x07orderid\x18\x01 \x01(\x04\x12\x0f\n\x07transid\x18\x02 \x01(\x04\"W\n#CInventory_PurchaseFinalize_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08language\x18\x02 \x01(\x05\x12\x0f\n\x07orderid\x18\x03 \x01(\x04\"Q\n\x1e\x43Inventory_InspectItem_Request\x12\x11\n\titemdefid\x18\x01 \x01(\x04\x12\x0e\n\x06itemid\x18\x02 \x01(\x06\x12\x0c\n\x04tags\x18\x03 \x01(\t\"i\n&CInventoryClient_NewItems_Notification\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x30\n\x12inventory_response\x18\x02 \x01(\x0b\x32\x14.CInventory_Response2\x9b\n\n\tInventory\x12\x46\n\x0cGetInventory\x12 .CInventory_GetInventory_Request\x1a\x14.CInventory_Response\x12\x46\n\x0c\x45xchangeItem\x12 .CInventory_ExchangeItem_Request\x1a\x14.CInventory_Response\x12}\n\x1aGetEligiblePromoItemDefIDs\x12..CInventory_GetEligiblePromoItemDefIDs_Request\x1a/.CInventory_GetEligiblePromoItemDefIDs_Response\x12\x41\n\x0c\x41\x64\x64PromoItem\x12\x1b.CInventory_AddItem_Request\x1a\x14.CInventory_Response\x12H\n\x0fSafeModifyItems\x12\x1f.CInventory_ModifyItems_Request\x1a\x14.CInventory_Response\x12L\n\x0f\x43onsumePlaytime\x12#.CInventory_ConsumePlaytime_Request\x1a\x14.CInventory_Response\x12\x44\n\x0b\x43onsumeItem\x12\x1f.CInventory_ConsumeItem_Request\x1a\x14.CInventory_Response\x12\x44\n\x0f\x44\x65vGenerateItem\x12\x1b.CInventory_AddItem_Request\x1a\x14.CInventory_Response\x12J\n\x0e\x44\x65vSetNextDrop\x12\".CInventory_DevSetNextDrop_Request\x1a\x14.CInventory_Response\x12J\n\x0eSplitItemStack\x12\".CInventory_SplitItemStack_Request\x1a\x14.CInventory_Response\x12P\n\x11\x43ombineItemStacks\x12%.CInventory_CombineItemStacks_Request\x1a\x14.CInventory_Response\x12Y\n\x0eGetItemDefMeta\x12\".CInventory_GetItemDefMeta_Request\x1a#.CInventory_GetItemDefMeta_Response\x12h\n\x13GetUserPurchaseInfo\x12\'.CInventory_GetUserPurchaseInfo_Request\x1a(.CInventory_GetUserPurchaseInfo_Response\x12S\n\x0cPurchaseInit\x12 .CInventory_PurchaseInit_Request\x1a!.CInventory_PurchaseInit_Response\x12N\n\x10PurchaseFinalize\x12$.CInventory_PurchaseFinalize_Request\x1a\x14.CInventory_Response\x12\x44\n\x0bInspectItem\x12\x1f.CInventory_InspectItem_Request\x1a\x14.CInventory_Response2_\n\x0fInventoryClient\x12\x46\n\x0eNotifyNewItems\x12\'.CInventoryClient_NewItems_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_inventory_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_INVENTORYCLIENT']._options = None
  _globals['_INVENTORYCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_CINVENTORY_GETINVENTORY_REQUEST']._serialized_start=93
  _globals['_CINVENTORY_GETINVENTORY_REQUEST']._serialized_end=158
  _globals['_CINVENTORY_RESPONSE']._serialized_start=161
  _globals['_CINVENTORY_RESPONSE']._serialized_end=295
  _globals['_CINVENTORY_EXCHANGEITEM_REQUEST']._serialized_start=298
  _globals['_CINVENTORY_EXCHANGEITEM_REQUEST']._serialized_end=440
  _globals['_CINVENTORY_GETELIGIBLEPROMOITEMDEFIDS_REQUEST']._serialized_start=442
  _globals['_CINVENTORY_GETELIGIBLEPROMOITEMDEFIDS_REQUEST']._serialized_end=521
  _globals['_CINVENTORY_GETELIGIBLEPROMOITEMDEFIDS_RESPONSE']._serialized_start=523
  _globals['_CINVENTORY_GETELIGIBLEPROMOITEMDEFIDS_RESPONSE']._serialized_end=591
  _globals['_CINVENTORY_ADDITEM_REQUEST']._serialized_start=594
  _globals['_CINVENTORY_ADDITEM_REQUEST']._serialized_end=808
  _globals['_CINVENTORY_MODIFYITEMS_REQUEST']._serialized_start=811
  _globals['_CINVENTORY_MODIFYITEMS_REQUEST']._serialized_end=1168
  _globals['_CINVENTORY_MODIFYITEMS_REQUEST_ITEMPROPERTYUPDATE']._serialized_start=966
  _globals['_CINVENTORY_MODIFYITEMS_REQUEST_ITEMPROPERTYUPDATE']._serialized_end=1168
  _globals['_CINVENTORY_CONSUMEPLAYTIME_REQUEST']._serialized_start=1170
  _globals['_CINVENTORY_CONSUMEPLAYTIME_REQUEST']._serialized_end=1240
  _globals['_CINVENTORY_CONSUMEITEM_REQUEST']._serialized_start=1243
  _globals['_CINVENTORY_CONSUMEITEM_REQUEST']._serialized_end=1379
  _globals['_CINVENTORY_DEVSETNEXTDROP_REQUEST']._serialized_start=1381
  _globals['_CINVENTORY_DEVSETNEXTDROP_REQUEST']._serialized_end=1468
  _globals['_CINVENTORY_SPLITITEMSTACK_REQUEST']._serialized_start=1470
  _globals['_CINVENTORY_SPLITITEMSTACK_REQUEST']._serialized_end=1571
  _globals['_CINVENTORY_COMBINEITEMSTACKS_REQUEST']._serialized_start=1574
  _globals['_CINVENTORY_COMBINEITEMSTACKS_REQUEST']._serialized_end=1702
  _globals['_CINVENTORY_GETITEMDEFMETA_REQUEST']._serialized_start=1704
  _globals['_CINVENTORY_GETITEMDEFMETA_REQUEST']._serialized_end=1754
  _globals['_CINVENTORY_GETITEMDEFMETA_RESPONSE']._serialized_start=1756
  _globals['_CINVENTORY_GETITEMDEFMETA_RESPONSE']._serialized_end=1826
  _globals['_CINVENTORY_GETUSERPURCHASEINFO_REQUEST']._serialized_start=1828
  _globals['_CINVENTORY_GETUSERPURCHASEINFO_REQUEST']._serialized_end=1868
  _globals['_CINVENTORY_GETUSERPURCHASEINFO_RESPONSE']._serialized_start=1870
  _globals['_CINVENTORY_GETUSERPURCHASEINFO_RESPONSE']._serialized_end=1930
  _globals['_CINVENTORY_PURCHASEINIT_REQUEST']._serialized_start=1933
  _globals['_CINVENTORY_PURCHASEINIT_REQUEST']._serialized_end=2111
  _globals['_CINVENTORY_PURCHASEINIT_REQUEST_LINEITEM']._serialized_start=2064
  _globals['_CINVENTORY_PURCHASEINIT_REQUEST_LINEITEM']._serialized_end=2111
  _globals['_CINVENTORY_PURCHASEINIT_RESPONSE']._serialized_start=2113
  _globals['_CINVENTORY_PURCHASEINIT_RESPONSE']._serialized_end=2181
  _globals['_CINVENTORY_PURCHASEFINALIZE_REQUEST']._serialized_start=2183
  _globals['_CINVENTORY_PURCHASEFINALIZE_REQUEST']._serialized_end=2270
  _globals['_CINVENTORY_INSPECTITEM_REQUEST']._serialized_start=2272
  _globals['_CINVENTORY_INSPECTITEM_REQUEST']._serialized_end=2353
  _globals['_CINVENTORYCLIENT_NEWITEMS_NOTIFICATION']._serialized_start=2355
  _globals['_CINVENTORYCLIENT_NEWITEMS_NOTIFICATION']._serialized_end=2460
  _globals['_INVENTORY']._serialized_start=2463
  _globals['_INVENTORY']._serialized_end=3770
  _globals['_INVENTORYCLIENT']._serialized_start=3772
  _globals['_INVENTORYCLIENT']._serialized_end=3867
_builder.BuildServices(DESCRIPTOR, 'steammessages_inventory_pb2', _globals)
# @@protoc_insertion_point(module_scope)
