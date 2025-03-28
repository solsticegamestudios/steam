# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_notifications.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steammessages_notifications.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x88\x02\n\x15SteamNotificationData\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x04\x12\x1c\n\x14notification_targets\x18\x02 \x01(\r\x12T\n\x11notification_type\x18\x03 \x01(\x0e\x32\x17.ESteamNotificationType: k_ESteamNotificationType_Invalid\x12\x11\n\tbody_data\x18\x04 \x01(\t\x12\x0c\n\x04read\x18\x07 \x01(\x08\x12\x11\n\ttimestamp\x18\x08 \x01(\r\x12\x0e\n\x06hidden\x18\t \x01(\x08\x12\x0e\n\x06\x65xpiry\x18\n \x01(\r\x12\x0e\n\x06viewed\x18\x0b \x01(\r\"\xc5\x01\n5CSteamNotification_NotificationsReceived_Notification\x12-\n\rnotifications\x18\x01 \x03(\x0b\x32\x16.SteamNotificationData\x12\x1a\n\x12pending_gift_count\x18\x02 \x01(\r\x12\x1c\n\x14pending_friend_count\x18\x03 \x01(\r\x12#\n\x1bpending_family_invite_count\x18\x04 \x01(\r\"\x91\x01\n\x1bSteamNotificationPreference\x12T\n\x11notification_type\x18\x01 \x01(\x0e\x32\x17.ESteamNotificationType: k_ESteamNotificationType_Invalid\x12\x1c\n\x14notification_targets\x18\x02 \x01(\r\"g\n2CSteamNotification_PreferencesUpdated_Notification\x12\x31\n\x0bpreferences\x18\x01 \x03(\x0b\x32\x1c.SteamNotificationPreference*\xf3\t\n\x16\x45SteamNotificationType\x12$\n k_ESteamNotificationType_Invalid\x10\x00\x12!\n\x1dk_ESteamNotificationType_Test\x10\x01\x12!\n\x1dk_ESteamNotificationType_Gift\x10\x02\x12$\n k_ESteamNotificationType_Comment\x10\x03\x12!\n\x1dk_ESteamNotificationType_Item\x10\x04\x12)\n%k_ESteamNotificationType_FriendInvite\x10\x05\x12&\n\"k_ESteamNotificationType_MajorSale\x10\x06\x12-\n)k_ESteamNotificationType_PreloadAvailable\x10\x07\x12%\n!k_ESteamNotificationType_Wishlist\x10\x08\x12\'\n#k_ESteamNotificationType_TradeOffer\x10\t\x12$\n k_ESteamNotificationType_General\x10\n\x12(\n$k_ESteamNotificationType_HelpRequest\x10\x0b\x12&\n\"k_ESteamNotificationType_AsyncGame\x10\x0c\x12$\n k_ESteamNotificationType_ChatMsg\x10\r\x12)\n%k_ESteamNotificationType_ModeratorMsg\x10\x0e\x12\x39\n5k_ESteamNotificationType_ParentalFeatureAccessRequest\x10\x0f\x12)\n%k_ESteamNotificationType_FamilyInvite\x10\x10\x12\x32\n.k_ESteamNotificationType_FamilyPurchaseRequest\x10\x11\x12\x34\n0k_ESteamNotificationType_ParentalPlaytimeRequest\x10\x12\x12:\n6k_ESteamNotificationType_FamilyPurchaseRequestResponse\x10\x13\x12:\n6k_ESteamNotificationType_ParentalFeatureAccessResponse\x10\x14\x12\x35\n1k_ESteamNotificationType_ParentalPlaytimeResponse\x10\x15\x12/\n+k_ESteamNotificationType_RequestedGameAdded\x10\x16\x12(\n$k_ESteamNotificationType_SendToPhone\x10\x17\x12+\n\'k_ESteamNotificationType_ClipDownloaded\x10\x18\x12&\n\"k_ESteamNotificationType_2FAPrompt\x10\x19\x12/\n+k_ESteamNotificationType_MobileConfirmation\x10\x1a\x12)\n%k_ESteamNotificationType_PartnerEvent\x10\x1b\x32\xd5\x01\n\x17SteamNotificationClient\x12\\\n\x15NotificationsReceived\x12\x36.CSteamNotification_NotificationsReceived_Notification\x1a\x0b.NoResponse\x12V\n\x12PreferencesUpdated\x12\x33.CSteamNotification_PreferencesUpdated_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_notifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_STEAMNOTIFICATIONCLIENT']._options = None
  _globals['_STEAMNOTIFICATIONCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_ESTEAMNOTIFICATIONTYPE']._serialized_start=818
  _globals['_ESTEAMNOTIFICATIONTYPE']._serialized_end=2085
  _globals['_STEAMNOTIFICATIONDATA']._serialized_start=98
  _globals['_STEAMNOTIFICATIONDATA']._serialized_end=362
  _globals['_CSTEAMNOTIFICATION_NOTIFICATIONSRECEIVED_NOTIFICATION']._serialized_start=365
  _globals['_CSTEAMNOTIFICATION_NOTIFICATIONSRECEIVED_NOTIFICATION']._serialized_end=562
  _globals['_STEAMNOTIFICATIONPREFERENCE']._serialized_start=565
  _globals['_STEAMNOTIFICATIONPREFERENCE']._serialized_end=710
  _globals['_CSTEAMNOTIFICATION_PREFERENCESUPDATED_NOTIFICATION']._serialized_start=712
  _globals['_CSTEAMNOTIFICATION_PREFERENCESUPDATED_NOTIFICATION']._serialized_end=815
  _globals['_STEAMNOTIFICATIONCLIENT']._serialized_start=2088
  _globals['_STEAMNOTIFICATIONCLIENT']._serialized_end=2301
_builder.BuildServices(DESCRIPTOR, 'steammessages_notifications_pb2', _globals)
# @@protoc_insertion_point(module_scope)
