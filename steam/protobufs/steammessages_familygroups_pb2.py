# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_familygroups.proto
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
import steam.protobufs.enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steammessages_familygroups.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x0b\x65nums.proto\"H\n\'CFamilyGroups_CreateFamilyGroup_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"a\n(CFamilyGroups_CreateFamilyGroup_Response\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x1d\n\x15\x63ooldown_skip_granted\x18\x02 \x01(\x08\"Y\n$CFamilyGroups_GetFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11send_running_apps\x18\x02 \x01(\x08\"\x97\x01\n\x11\x46\x61milyGroupMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\x12\x13\n\x0btime_joined\x18\x03 \x01(\r\x12\"\n\x1a\x63ooldown_seconds_remaining\x18\x04 \x01(\r\"e\n\x18\x46\x61milyGroupPendingInvite\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\"*\n\x17\x46\x61milyGroupFormerMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xaf\x02\n%CFamilyGroups_GetFamilyGroup_Response\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x07members\x18\x02 \x03(\x0b\x32\x12.FamilyGroupMember\x12\x32\n\x0fpending_invites\x18\x03 \x03(\x0b\x32\x19.FamilyGroupPendingInvite\x12\x12\n\nfree_spots\x18\x04 \x01(\r\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\'\n\x1fslot_cooldown_remaining_seconds\x18\x06 \x01(\r\x12\x30\n\x0e\x66ormer_members\x18\x07 \x03(\x0b\x32\x18.FamilyGroupFormerMember\x12\x1f\n\x17slot_cooldown_overrides\x18\x08 \x01(\r\"e\n+CFamilyGroups_GetFamilyGroupForUser_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x04\x12%\n\x1dinclude_family_group_response\x18\x02 \x01(\x08\"\xa2\x01\n\x1f\x46\x61milyGroupPendingInviteForUser\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x38\n\x04role\x18\x02 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\x12\x17\n\x0finviter_steamid\x18\x03 \x01(\x06\x12\x14\n\x0c\x61waiting_2fa\x18\x04 \x01(\x08\"\x86\x03\n,CFamilyGroups_GetFamilyGroupForUser_Response\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\"\n\x1ais_not_member_of_any_group\x18\x02 \x01(\x08\x12\x1a\n\x12latest_time_joined\x18\x03 \x01(\r\x12$\n\x1clatest_joined_family_groupid\x18\x04 \x01(\x04\x12?\n\x15pending_group_invites\x18\x05 \x03(\x0b\x32 .FamilyGroupPendingInviteForUser\x12\x0c\n\x04role\x18\x06 \x01(\r\x12\"\n\x1a\x63ooldown_seconds_remaining\x18\x07 \x01(\r\x12<\n\x0c\x66\x61mily_group\x18\x08 \x01(\x0b\x32&.CFamilyGroups_GetFamilyGroup_Response\x12\'\n\x1f\x63\x61n_undelete_last_joined_family\x18\t \x01(\x08\"V\n.CFamilyGroups_ModifyFamilyGroupDetails_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n/CFamilyGroups_ModifyFamilyGroupDetails_Response\"\xa0\x01\n)CFamilyGroups_InviteToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x18\n\x10receiver_steamid\x18\x02 \x01(\x06\x12\x41\n\rreceiver_role\x18\x03 \x01(\x0e\x32\x11.EFamilyGroupRole:\x17k_EFamilyGroupRole_None\"\x9d\x01\n*CFamilyGroups_InviteToFamilyGroup_Response\x12\x11\n\tinvite_id\x18\x01 \x01(\x04\x12\\\n\x11two_factor_method\x18\x02 \x01(\x0e\x32\x1d.EFamilyGroupsTwoFactorMethod:\"k_EFamilyGroupsTwoFactorMethodNone\"l\n0CFamilyGroups_ConfirmInviteToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x11\n\tinvite_id\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\"3\n1CFamilyGroups_ConfirmInviteToFamilyGroup_Response\"^\n3CFamilyGroups_ResendInvitationToFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x04\"6\n4CFamilyGroups_ResendInvitationToFamilyGroup_Response\"N\n%CFamilyGroups_JoinFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\r\n\x05nonce\x18\x02 \x01(\x04\"\xc6\x01\n&CFamilyGroups_JoinFamilyGroup_Response\x12\\\n\x11two_factor_method\x18\x02 \x01(\x0e\x32\x1d.EFamilyGroupsTwoFactorMethod:\"k_EFamilyGroupsTwoFactorMethodNone\x12\x1d\n\x15\x63ooldown_skip_granted\x18\x03 \x01(\x08\x12\x1f\n\x17invite_already_accepted\x18\x04 \x01(\x08\"h\n,CFamilyGroups_ConfirmJoinFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x11\n\tinvite_id\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\"/\n-CFamilyGroups_ConfirmJoinFamilyGroup_Response\"`\n+CFamilyGroups_RemoveFromFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11steamid_to_remove\x18\x02 \x01(\x06\".\n,CFamilyGroups_RemoveFromFamilyGroup_Response\"b\n-CFamilyGroups_CancelFamilyGroupInvite_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x19\n\x11steamid_to_cancel\x18\x02 \x01(\x06\"0\n.CFamilyGroups_CancelFamilyGroupInvite_Response\"a\n+CFamilyGroups_GetUsersSharingDevice_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x1a\n\x12\x63lient_instance_id\x18\x02 \x01(\x04\"=\n,CFamilyGroups_GetUsersSharingDevice_Response\x12\r\n\x05users\x18\x01 \x03(\x06\"A\n\'CFamilyGroups_DeleteFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"*\n(CFamilyGroups_DeleteFamilyGroup_Response\"C\n)CFamilyGroups_UndeleteFamilyGroup_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\",\n*CFamilyGroups_UndeleteFamilyGroup_Response\"B\n(CFamilyGroups_GetPlaytimeSummary_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x06\"\x82\x01\n\x1b\x43\x46\x61milyGroups_PlaytimeEntry\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x14\n\x0c\x66irst_played\x18\x03 \x01(\r\x12\x15\n\rlatest_played\x18\x04 \x01(\r\x12\x16\n\x0eseconds_played\x18\x05 \x01(\r\"\x92\x01\n)CFamilyGroups_GetPlaytimeSummary_Response\x12-\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1c.CFamilyGroups_PlaytimeEntry\x12\x36\n\x10\x65ntries_by_owner\x18\x02 \x03(\x0b\x32\x1c.CFamilyGroups_PlaytimeEntry\"\x8e\x01\n%CFamilyGroups_RequestPurchase_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x17\n\x0fgidshoppingcart\x18\x02 \x01(\x04\x12\x1a\n\x12store_country_code\x18\x03 \x01(\t\x12\x18\n\x10use_account_cart\x18\x04 \x01(\x08\"U\n&CFamilyGroups_RequestPurchase_Response\x12\x17\n\x0fgidshoppingcart\x18\x01 \x01(\x04\x12\x12\n\nrequest_id\x18\x02 \x01(\x04\"|\n)CFamilyGroups_GetPurchaseRequests_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x13\n\x0brequest_ids\x18\x03 \x03(\x04\x12\"\n\x1art_include_completed_since\x18\x04 \x01(\r\"\x81\x03\n\x0fPurchaseRequest\x12\x19\n\x11requester_steamid\x18\x01 \x01(\x06\x12\x17\n\x0fgidshoppingcart\x18\x02 \x01(\x04\x12\x16\n\x0etime_requested\x18\x03 \x01(\r\x12\x16\n\x0etime_responded\x18\x04 \x01(\r\x12\x19\n\x11responder_steamid\x18\x05 \x01(\x06\x12O\n\x0fresponse_action\x18\x06 \x01(\x0e\x32\x17.EPurchaseRequestAction:\x1dk_EPurchaseRequestAction_None\x12\x14\n\x0cis_completed\x18\x07 \x01(\x08\x12\x12\n\nrequest_id\x18\x08 \x01(\x04\x12\x1c\n\x14requested_packageids\x18\t \x03(\r\x12\x1c\n\x14purchased_packageids\x18\n \x03(\r\x12\x1b\n\x13requested_bundleids\x18\x0b \x03(\r\x12\x1b\n\x13purchased_bundleids\x18\x0c \x03(\r\"P\n*CFamilyGroups_GetPurchaseRequests_Response\x12\"\n\x08requests\x18\x01 \x03(\x0b\x32\x10.PurchaseRequest\"\xa6\x01\n0CFamilyGroups_RespondToRequestedPurchase_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x46\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x17.EPurchaseRequestAction:\x1dk_EPurchaseRequestAction_None\x12\x12\n\nrequest_id\x18\x04 \x01(\x04\"3\n1CFamilyGroups_RespondToRequestedPurchase_Response\"<\n\"CFamilyGroups_GetChangeLog_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"\xf9\x01\n#CFamilyGroups_GetChangeLog_Response\x12<\n\x07\x63hanges\x18\x01 \x03(\x0b\x32+.CFamilyGroups_GetChangeLog_Response.Change\x1a\x93\x01\n\x06\x43hange\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\x15\n\ractor_steamid\x18\x02 \x01(\x06\x12=\n\x04type\x18\x03 \x01(\x0e\x32\x1a.EFamilyGroupChangeLogType:\x13k_InvalidChangeType\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x12\n\nby_support\x18\x05 \x01(\x08\"b\n0CFamilyGroups_SetFamilyCooldownOverrides_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x16\n\x0e\x63ooldown_count\x18\x02 \x01(\r\"3\n1CFamilyGroups_SetFamilyCooldownOverrides_Response\"\xc3\x01\n*CFamilyGroups_GetSharedLibraryApps_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x06\x12\x13\n\x0binclude_own\x18\x02 \x01(\x08\x12\x18\n\x10include_excluded\x18\x03 \x01(\x08\x12\x10\n\x08language\x18\x05 \x01(\t\x12\x10\n\x08max_apps\x18\x06 \x01(\r\x12\x19\n\x11include_non_games\x18\x07 \x01(\x08\x12\x0f\n\x07steamid\x18\x08 \x01(\x06\"\xf6\x03\n+CFamilyGroups_GetSharedLibraryApps_Response\x12\x44\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x36.CFamilyGroups_GetSharedLibraryApps_Response.SharedApp\x12\x15\n\rowner_steamid\x18\x02 \x01(\x06\x1a\xe9\x02\n\tSharedApp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x16\n\x0eowner_steamids\x18\x02 \x03(\x06\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07sort_as\x18\x07 \x01(\t\x12\x18\n\x10\x63\x61psule_filename\x18\x08 \x01(\t\x12\x15\n\rimg_icon_hash\x18\t \x01(\t\x12O\n\x0e\x65xclude_reason\x18\n \x01(\x0e\x32\x1c.ESharedLibraryExcludeReason:\x19k_ESharedLibrary_Included\x12\x18\n\x10rt_time_acquired\x18\x0b \x01(\r\x12\x16\n\x0ert_last_played\x18\x0c \x01(\r\x12\x13\n\x0brt_playtime\x18\r \x01(\r\x12\x30\n\x08\x61pp_type\x18\x0e \x01(\x0e\x32\x0e.EProtoAppType:\x0ek_EAppTypeGame\x12\x1b\n\x13\x63ontent_descriptors\x18\x0f \x03(\r\"i\n(CFamilyGroups_SetPreferredLender_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x16\n\x0elender_steamid\x18\x03 \x01(\x06\"+\n)CFamilyGroups_SetPreferredLender_Response\"C\n)CFamilyGroups_GetPreferredLenders_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\"\xb2\x01\n*CFamilyGroups_GetPreferredLenders_Response\x12I\n\x07members\x18\x01 \x03(\x0b\x32\x38.CFamilyGroups_GetPreferredLenders_Response.FamilyMember\x1a\x39\n\x0c\x46\x61milyMember\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10preferred_appids\x18\x02 \x03(\r\"R\n\'CFamilyGroups_ForceAcceptInvite_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"*\n(CFamilyGroups_ForceAcceptInvite_Response\"V\n+CFamilyGroups_GetInviteCheckResults_Request\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"z\n,CFamilyGroups_GetInviteCheckResults_Response\x12\x1e\n\x16wallet_country_matches\x18\x01 \x01(\x08\x12\x10\n\x08ip_match\x18\x02 \x01(\x08\x12\x18\n\x10join_restriction\x18\x03 \x01(\r\"M\n\'CFamilyGroups_ClearCooldownSkip_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x11\n\tinvite_id\x18\x02 \x01(\x04\"*\n(CFamilyGroups_ClearCooldownSkip_Response\"\xdb\x02\n2CFamilyGroupsClient_NotifyRunningApps_Notification\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04\x12T\n\x0crunning_apps\x18\x02 \x03(\x0b\x32>.CFamilyGroupsClient_NotifyRunningApps_Notification.RunningApp\x1a>\n\rPlayingMember\x12\x16\n\x0emember_steamid\x18\x01 \x01(\x06\x12\x15\n\rowner_steamid\x18\x02 \x01(\x06\x1aw\n\nRunningApp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12Z\n\x0fplaying_members\x18\x03 \x03(\x0b\x32\x41.CFamilyGroupsClient_NotifyRunningApps_Notification.PlayingMember\"/\n-CFamilyGroupsClient_InviteStatus_Notification\"G\n-CFamilyGroupsClient_GroupChanged_Notification\x12\x16\n\x0e\x66\x61mily_groupid\x18\x01 \x01(\x04*\x87\x01\n\x10\x45\x46\x61milyGroupRole\x12\x1b\n\x17k_EFamilyGroupRole_None\x10\x00\x12\x1c\n\x18k_EFamilyGroupRole_Adult\x10\x01\x12\x1c\n\x18k_EFamilyGroupRole_Child\x10\x02\x12\x1a\n\x16k_EFamilyGroupRole_MAX\x10\x03*\x99\x01\n\x1c\x45\x46\x61milyGroupsTwoFactorMethod\x12&\n\"k_EFamilyGroupsTwoFactorMethodNone\x10\x00\x12(\n$k_EFamilyGroupsTwoFactorMethodMobile\x10\x01\x12\'\n#k_EFamilyGroupsTwoFactorMethodEmail\x10\x02*\xf8\x01\n\x16\x45PurchaseRequestAction\x12!\n\x1dk_EPurchaseRequestAction_None\x10\x00\x12$\n k_EPurchaseRequestAction_Decline\x10\x01\x12&\n\"k_EPurchaseRequestAction_Purchased\x10\x02\x12&\n\"k_EPurchaseRequestAction_Abandoned\x10\x03\x12#\n\x1fk_EPurchaseRequestAction_Cancel\x10\x04\x12 \n\x1ck_EPurchaseRequestAction_MAX\x10\x05*\x88\x06\n\x19\x45\x46\x61milyGroupChangeLogType\x12\x17\n\x13k_InvalidChangeType\x10\x00\x12\x18\n\x14k_FamilyGroupCreated\x10\x01\x12\x19\n\x15k_FamilyGroupModified\x10\x02\x12\x18\n\x14k_FamilyGroupDeleted\x10\x03\x12\x14\n\x10k_AccountInvited\x10\x04\x12\x1d\n\x19k_InviteDeniedByGroupSize\x10\x05\x12\x17\n\x13k_JoinedFamilyGroup\x10\x06\x12 \n\x1ck_JoinDeniedByRegionMismatch\x10\x07\x12\"\n\x1ek_JoinDeniedByMissingIpAddress\x10\x08\x12 \n\x1ck_JoinDeniedByFamilyCooldown\x10\t\x12\x1e\n\x1ak_JoinDeniedByUserCooldown\x10\n\x12\x1c\n\x18k_JoinDeniedByOtherGroup\x10\x0b\x12\x14\n\x10k_AccountRemoved\x10\x0c\x12\x14\n\x10k_InviteCanceled\x10\r\x12\x17\n\x13k_PurchaseRequested\x10\x0e\x12\x1d\n\x19k_ParentalSettingsEnabled\x10\x0f\x12\x1e\n\x1ak_ParentalSettingsDisabled\x10\x10\x12\x1d\n\x19k_ParentalSettingsChanged\x10\x11\x12$\n k_FamilyCooldownOverridesChanged\x10\x12\x12\x1d\n\x19k_PurchaseRequestCanceled\x10\x13\x12\x1d\n\x19k_PurchaseRequestApproved\x10\x14\x12\x1d\n\x19k_PurchaseRequestDeclined\x10\x15\x12\x1a\n\x16k_CooldownSkipConsumed\x10\x16\x12\x19\n\x15k_FamilyGroupRestored\x10\x17\x12\x10\n\x0ck_JoinDenied\x10\x18\x12 \n\x1ck_SupportForceAcceptedInvite\x10\x19*\x9c\x0b\n\x1b\x45SharedLibraryExcludeReason\x12\x1d\n\x19k_ESharedLibrary_Included\x10\x00\x12*\n&k_ESharedLibrary_AppExcluded_ByPartner\x10\x01\x12$\n k_ESharedLibrary_LicenseExcluded\x10\x02\x12\x1d\n\x19k_ESharedLibrary_FreeGame\x10\x03\x12#\n\x1fk_ESharedLibrary_LicensePrivate\x10\x04\x12-\n)k_ESharedLibrary_AppExcluded_WrongAppType\x10\x06\x12\x31\n-k_ESharedLibrary_AppExcluded_NonrefundableDLC\x10\x07\x12.\n*k_ESharedLibrary_AppExcluded_UnreleasedApp\x10\x08\x12\x32\n.k_ESharedLibrary_AppExcluded_ParentAppExcluded\x10\t\x12.\n*k_ESharedLibrary_PackageExcluded_ByPartner\x10\n\x12,\n(k_ESharedLibrary_PackageExcluded_Special\x10\x0b\x12(\n$k_ESharedLibrary_PackageExcluded_Dev\x10\x0c\x12\x30\n,k_ESharedLibrary_PackageExcluded_FreeWeekend\x10\r\x12,\n(k_ESharedLibrary_PackageExcluded_Invalid\x10\x0f\x12\x35\n1k_ESharedLibrary_PackageExcluded_RecurringLicense\x10\x10\x12\x35\n1k_ESharedLibrary_PackageExcluded_WrongLicenseType\x10\x11\x12.\n*k_ESharedLibrary_PackageExcluded_MasterSub\x10\x12\x12\x34\n0k_ESharedLibrary_PackageExcluded_NoShareableApps\x10\x13\x12\x35\n1k_ESharedLibrary_LicenseExcluded_PaymentMasterSub\x10\x14\x12\x37\n3k_ESharedLibrary_LicenseExcluded_PaymentFamilyGroup\x10\x15\x12<\n8k_ESharedLibrary_LicenseExcluded_PaymentAuthorizedDevice\x10\x16\x12\x35\n1k_ESharedLibrary_LicenseExcluded_PaymentAutoGrant\x10\x17\x12\x30\n,k_ESharedLibrary_LicenseExcluded_FlagPending\x10\x18\x12\x36\n2k_ESharedLibrary_LicenseExcluded_FlagPendingRefund\x10\x19\x12\x31\n-k_ESharedLibrary_LicenseExcluded_FlagBorrowed\x10\x1a\x12\x32\n.k_ESharedLibrary_LicenseExcluded_FlagAutoGrant\x10\x1b\x12\x33\n/k_ESharedLibrary_LicenseExcluded_FlagTimedTrial\x10\x1c\x12,\n(k_ESharedLibrary_LicenseExcluded_FreeSub\x10\x1d\x12-\n)k_ESharedLibrary_LicenseExcluded_Inactive\x10\x1e\x32\xb4\x17\n\x0c\x46\x61milyGroups\x12h\n\x11\x43reateFamilyGroup\x12(.CFamilyGroups_CreateFamilyGroup_Request\x1a).CFamilyGroups_CreateFamilyGroup_Response\x12_\n\x0eGetFamilyGroup\x12%.CFamilyGroups_GetFamilyGroup_Request\x1a&.CFamilyGroups_GetFamilyGroup_Response\x12t\n\x15GetFamilyGroupForUser\x12,.CFamilyGroups_GetFamilyGroupForUser_Request\x1a-.CFamilyGroups_GetFamilyGroupForUser_Response\x12}\n\x18ModifyFamilyGroupDetails\x12/.CFamilyGroups_ModifyFamilyGroupDetails_Request\x1a\x30.CFamilyGroups_ModifyFamilyGroupDetails_Response\x12n\n\x13InviteToFamilyGroup\x12*.CFamilyGroups_InviteToFamilyGroup_Request\x1a+.CFamilyGroups_InviteToFamilyGroup_Response\x12\x83\x01\n\x1a\x43onfirmInviteToFamilyGroup\x12\x31.CFamilyGroups_ConfirmInviteToFamilyGroup_Request\x1a\x32.CFamilyGroups_ConfirmInviteToFamilyGroup_Response\x12\x8c\x01\n\x1dResendInvitationToFamilyGroup\x12\x34.CFamilyGroups_ResendInvitationToFamilyGroup_Request\x1a\x35.CFamilyGroups_ResendInvitationToFamilyGroup_Response\x12\x62\n\x0fJoinFamilyGroup\x12&.CFamilyGroups_JoinFamilyGroup_Request\x1a\'.CFamilyGroups_JoinFamilyGroup_Response\x12w\n\x16\x43onfirmJoinFamilyGroup\x12-.CFamilyGroups_ConfirmJoinFamilyGroup_Request\x1a..CFamilyGroups_ConfirmJoinFamilyGroup_Response\x12t\n\x15RemoveFromFamilyGroup\x12,.CFamilyGroups_RemoveFromFamilyGroup_Request\x1a-.CFamilyGroups_RemoveFromFamilyGroup_Response\x12z\n\x17\x43\x61ncelFamilyGroupInvite\x12..CFamilyGroups_CancelFamilyGroupInvite_Request\x1a/.CFamilyGroups_CancelFamilyGroupInvite_Response\x12t\n\x15GetUsersSharingDevice\x12,.CFamilyGroups_GetUsersSharingDevice_Request\x1a-.CFamilyGroups_GetUsersSharingDevice_Response\x12h\n\x11\x44\x65leteFamilyGroup\x12(.CFamilyGroups_DeleteFamilyGroup_Request\x1a).CFamilyGroups_DeleteFamilyGroup_Response\x12n\n\x13UndeleteFamilyGroup\x12*.CFamilyGroups_UndeleteFamilyGroup_Request\x1a+.CFamilyGroups_UndeleteFamilyGroup_Response\x12k\n\x12GetPlaytimeSummary\x12).CFamilyGroups_GetPlaytimeSummary_Request\x1a*.CFamilyGroups_GetPlaytimeSummary_Response\x12\x62\n\x0fRequestPurchase\x12&.CFamilyGroups_RequestPurchase_Request\x1a\'.CFamilyGroups_RequestPurchase_Response\x12n\n\x13GetPurchaseRequests\x12*.CFamilyGroups_GetPurchaseRequests_Request\x1a+.CFamilyGroups_GetPurchaseRequests_Response\x12\x83\x01\n\x1aRespondToRequestedPurchase\x12\x31.CFamilyGroups_RespondToRequestedPurchase_Request\x1a\x32.CFamilyGroups_RespondToRequestedPurchase_Response\x12Y\n\x0cGetChangeLog\x12#.CFamilyGroups_GetChangeLog_Request\x1a$.CFamilyGroups_GetChangeLog_Response\x12\x83\x01\n\x1aSetFamilyCooldownOverrides\x12\x31.CFamilyGroups_SetFamilyCooldownOverrides_Request\x1a\x32.CFamilyGroups_SetFamilyCooldownOverrides_Response\x12q\n\x14GetSharedLibraryApps\x12+.CFamilyGroups_GetSharedLibraryApps_Request\x1a,.CFamilyGroups_GetSharedLibraryApps_Response\x12k\n\x12SetPreferredLender\x12).CFamilyGroups_SetPreferredLender_Request\x1a*.CFamilyGroups_SetPreferredLender_Response\x12n\n\x13GetPreferredLenders\x12*.CFamilyGroups_GetPreferredLenders_Request\x1a+.CFamilyGroups_GetPreferredLenders_Response\x12h\n\x11\x46orceAcceptInvite\x12(.CFamilyGroups_ForceAcceptInvite_Request\x1a).CFamilyGroups_ForceAcceptInvite_Response\x12t\n\x15GetInviteCheckResults\x12,.CFamilyGroups_GetInviteCheckResults_Request\x1a-.CFamilyGroups_GetInviteCheckResults_Response\x12h\n\x11\x43learCooldownSkip\x12(.CFamilyGroups_ClearCooldownSkip_Request\x1a).CFamilyGroups_ClearCooldownSkip_Response2\x97\x02\n\x12\x46\x61milyGroupsClient\x12U\n\x11NotifyRunningApps\x12\x33.CFamilyGroupsClient_NotifyRunningApps_Notification\x1a\x0b.NoResponse\x12Q\n\x12NotifyInviteStatus\x12..CFamilyGroupsClient_InviteStatus_Notification\x1a\x0b.NoResponse\x12Q\n\x12NotifyGroupChanged\x12..CFamilyGroupsClient_GroupChanged_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_familygroups_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_FAMILYGROUPSCLIENT']._options = None
  _globals['_FAMILYGROUPSCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_EFAMILYGROUPROLE']._serialized_start=7446
  _globals['_EFAMILYGROUPROLE']._serialized_end=7581
  _globals['_EFAMILYGROUPSTWOFACTORMETHOD']._serialized_start=7584
  _globals['_EFAMILYGROUPSTWOFACTORMETHOD']._serialized_end=7737
  _globals['_EPURCHASEREQUESTACTION']._serialized_start=7740
  _globals['_EPURCHASEREQUESTACTION']._serialized_end=7988
  _globals['_EFAMILYGROUPCHANGELOGTYPE']._serialized_start=7991
  _globals['_EFAMILYGROUPCHANGELOGTYPE']._serialized_end=8767
  _globals['_ESHAREDLIBRARYEXCLUDEREASON']._serialized_start=8770
  _globals['_ESHAREDLIBRARYEXCLUDEREASON']._serialized_end=10206
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_REQUEST']._serialized_start=109
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_REQUEST']._serialized_end=181
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_RESPONSE']._serialized_start=183
  _globals['_CFAMILYGROUPS_CREATEFAMILYGROUP_RESPONSE']._serialized_end=280
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_REQUEST']._serialized_start=282
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_REQUEST']._serialized_end=371
  _globals['_FAMILYGROUPMEMBER']._serialized_start=374
  _globals['_FAMILYGROUPMEMBER']._serialized_end=525
  _globals['_FAMILYGROUPPENDINGINVITE']._serialized_start=527
  _globals['_FAMILYGROUPPENDINGINVITE']._serialized_end=628
  _globals['_FAMILYGROUPFORMERMEMBER']._serialized_start=630
  _globals['_FAMILYGROUPFORMERMEMBER']._serialized_end=672
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_RESPONSE']._serialized_start=675
  _globals['_CFAMILYGROUPS_GETFAMILYGROUP_RESPONSE']._serialized_end=978
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_REQUEST']._serialized_start=980
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_REQUEST']._serialized_end=1081
  _globals['_FAMILYGROUPPENDINGINVITEFORUSER']._serialized_start=1084
  _globals['_FAMILYGROUPPENDINGINVITEFORUSER']._serialized_end=1246
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_RESPONSE']._serialized_start=1249
  _globals['_CFAMILYGROUPS_GETFAMILYGROUPFORUSER_RESPONSE']._serialized_end=1639
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_REQUEST']._serialized_start=1641
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_REQUEST']._serialized_end=1727
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_RESPONSE']._serialized_start=1729
  _globals['_CFAMILYGROUPS_MODIFYFAMILYGROUPDETAILS_RESPONSE']._serialized_end=1778
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_REQUEST']._serialized_start=1781
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_REQUEST']._serialized_end=1941
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_RESPONSE']._serialized_start=1944
  _globals['_CFAMILYGROUPS_INVITETOFAMILYGROUP_RESPONSE']._serialized_end=2101
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_REQUEST']._serialized_start=2103
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_REQUEST']._serialized_end=2211
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_RESPONSE']._serialized_start=2213
  _globals['_CFAMILYGROUPS_CONFIRMINVITETOFAMILYGROUP_RESPONSE']._serialized_end=2264
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_REQUEST']._serialized_start=2266
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_REQUEST']._serialized_end=2360
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_RESPONSE']._serialized_start=2362
  _globals['_CFAMILYGROUPS_RESENDINVITATIONTOFAMILYGROUP_RESPONSE']._serialized_end=2416
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_REQUEST']._serialized_start=2418
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_REQUEST']._serialized_end=2496
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_RESPONSE']._serialized_start=2499
  _globals['_CFAMILYGROUPS_JOINFAMILYGROUP_RESPONSE']._serialized_end=2697
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_REQUEST']._serialized_start=2699
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_REQUEST']._serialized_end=2803
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_RESPONSE']._serialized_start=2805
  _globals['_CFAMILYGROUPS_CONFIRMJOINFAMILYGROUP_RESPONSE']._serialized_end=2852
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_REQUEST']._serialized_start=2854
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_REQUEST']._serialized_end=2950
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_RESPONSE']._serialized_start=2952
  _globals['_CFAMILYGROUPS_REMOVEFROMFAMILYGROUP_RESPONSE']._serialized_end=2998
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_REQUEST']._serialized_start=3000
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_REQUEST']._serialized_end=3098
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_RESPONSE']._serialized_start=3100
  _globals['_CFAMILYGROUPS_CANCELFAMILYGROUPINVITE_RESPONSE']._serialized_end=3148
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_REQUEST']._serialized_start=3150
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_REQUEST']._serialized_end=3247
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_RESPONSE']._serialized_start=3249
  _globals['_CFAMILYGROUPS_GETUSERSSHARINGDEVICE_RESPONSE']._serialized_end=3310
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_REQUEST']._serialized_start=3312
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_REQUEST']._serialized_end=3377
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_RESPONSE']._serialized_start=3379
  _globals['_CFAMILYGROUPS_DELETEFAMILYGROUP_RESPONSE']._serialized_end=3421
  _globals['_CFAMILYGROUPS_UNDELETEFAMILYGROUP_REQUEST']._serialized_start=3423
  _globals['_CFAMILYGROUPS_UNDELETEFAMILYGROUP_REQUEST']._serialized_end=3490
  _globals['_CFAMILYGROUPS_UNDELETEFAMILYGROUP_RESPONSE']._serialized_start=3492
  _globals['_CFAMILYGROUPS_UNDELETEFAMILYGROUP_RESPONSE']._serialized_end=3536
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_REQUEST']._serialized_start=3538
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_REQUEST']._serialized_end=3604
  _globals['_CFAMILYGROUPS_PLAYTIMEENTRY']._serialized_start=3607
  _globals['_CFAMILYGROUPS_PLAYTIMEENTRY']._serialized_end=3737
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_RESPONSE']._serialized_start=3740
  _globals['_CFAMILYGROUPS_GETPLAYTIMESUMMARY_RESPONSE']._serialized_end=3886
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_REQUEST']._serialized_start=3889
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_REQUEST']._serialized_end=4031
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_RESPONSE']._serialized_start=4033
  _globals['_CFAMILYGROUPS_REQUESTPURCHASE_RESPONSE']._serialized_end=4118
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_REQUEST']._serialized_start=4120
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_REQUEST']._serialized_end=4244
  _globals['_PURCHASEREQUEST']._serialized_start=4247
  _globals['_PURCHASEREQUEST']._serialized_end=4632
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_RESPONSE']._serialized_start=4634
  _globals['_CFAMILYGROUPS_GETPURCHASEREQUESTS_RESPONSE']._serialized_end=4714
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_REQUEST']._serialized_start=4717
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_REQUEST']._serialized_end=4883
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_RESPONSE']._serialized_start=4885
  _globals['_CFAMILYGROUPS_RESPONDTOREQUESTEDPURCHASE_RESPONSE']._serialized_end=4936
  _globals['_CFAMILYGROUPS_GETCHANGELOG_REQUEST']._serialized_start=4938
  _globals['_CFAMILYGROUPS_GETCHANGELOG_REQUEST']._serialized_end=4998
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE']._serialized_start=5001
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE']._serialized_end=5250
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE_CHANGE']._serialized_start=5103
  _globals['_CFAMILYGROUPS_GETCHANGELOG_RESPONSE_CHANGE']._serialized_end=5250
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_REQUEST']._serialized_start=5252
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_REQUEST']._serialized_end=5350
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_RESPONSE']._serialized_start=5352
  _globals['_CFAMILYGROUPS_SETFAMILYCOOLDOWNOVERRIDES_RESPONSE']._serialized_end=5403
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_REQUEST']._serialized_start=5406
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_REQUEST']._serialized_end=5601
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE']._serialized_start=5604
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE']._serialized_end=6106
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE_SHAREDAPP']._serialized_start=5745
  _globals['_CFAMILYGROUPS_GETSHAREDLIBRARYAPPS_RESPONSE_SHAREDAPP']._serialized_end=6106
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_REQUEST']._serialized_start=6108
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_REQUEST']._serialized_end=6213
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_RESPONSE']._serialized_start=6215
  _globals['_CFAMILYGROUPS_SETPREFERREDLENDER_RESPONSE']._serialized_end=6258
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_REQUEST']._serialized_start=6260
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_REQUEST']._serialized_end=6327
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE']._serialized_start=6330
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE']._serialized_end=6508
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE_FAMILYMEMBER']._serialized_start=6451
  _globals['_CFAMILYGROUPS_GETPREFERREDLENDERS_RESPONSE_FAMILYMEMBER']._serialized_end=6508
  _globals['_CFAMILYGROUPS_FORCEACCEPTINVITE_REQUEST']._serialized_start=6510
  _globals['_CFAMILYGROUPS_FORCEACCEPTINVITE_REQUEST']._serialized_end=6592
  _globals['_CFAMILYGROUPS_FORCEACCEPTINVITE_RESPONSE']._serialized_start=6594
  _globals['_CFAMILYGROUPS_FORCEACCEPTINVITE_RESPONSE']._serialized_end=6636
  _globals['_CFAMILYGROUPS_GETINVITECHECKRESULTS_REQUEST']._serialized_start=6638
  _globals['_CFAMILYGROUPS_GETINVITECHECKRESULTS_REQUEST']._serialized_end=6724
  _globals['_CFAMILYGROUPS_GETINVITECHECKRESULTS_RESPONSE']._serialized_start=6726
  _globals['_CFAMILYGROUPS_GETINVITECHECKRESULTS_RESPONSE']._serialized_end=6848
  _globals['_CFAMILYGROUPS_CLEARCOOLDOWNSKIP_REQUEST']._serialized_start=6850
  _globals['_CFAMILYGROUPS_CLEARCOOLDOWNSKIP_REQUEST']._serialized_end=6927
  _globals['_CFAMILYGROUPS_CLEARCOOLDOWNSKIP_RESPONSE']._serialized_start=6929
  _globals['_CFAMILYGROUPS_CLEARCOOLDOWNSKIP_RESPONSE']._serialized_end=6971
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION']._serialized_start=6974
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION']._serialized_end=7321
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_PLAYINGMEMBER']._serialized_start=7138
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_PLAYINGMEMBER']._serialized_end=7200
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_RUNNINGAPP']._serialized_start=7202
  _globals['_CFAMILYGROUPSCLIENT_NOTIFYRUNNINGAPPS_NOTIFICATION_RUNNINGAPP']._serialized_end=7321
  _globals['_CFAMILYGROUPSCLIENT_INVITESTATUS_NOTIFICATION']._serialized_start=7323
  _globals['_CFAMILYGROUPSCLIENT_INVITESTATUS_NOTIFICATION']._serialized_end=7370
  _globals['_CFAMILYGROUPSCLIENT_GROUPCHANGED_NOTIFICATION']._serialized_start=7372
  _globals['_CFAMILYGROUPSCLIENT_GROUPCHANGED_NOTIFICATION']._serialized_end=7443
  _globals['_FAMILYGROUPS']._serialized_start=10209
  _globals['_FAMILYGROUPS']._serialized_end=13205
  _globals['_FAMILYGROUPSCLIENT']._serialized_start=13208
  _globals['_FAMILYGROUPSCLIENT']._serialized_end=13487
_builder.BuildServices(DESCRIPTOR, 'steammessages_familygroups_pb2', _globals)
# @@protoc_insertion_point(module_scope)
