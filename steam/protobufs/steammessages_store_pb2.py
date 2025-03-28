# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_store.proto
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
import steam.protobufs.contenthubs_pb2 as contenthubs__pb2
import steam.protobufs.enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19steammessages_store.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x11\x63ontenthubs.proto\x1a\x0b\x65nums.proto\"r\n\x1c\x43Store_RegisterCDKey_Request\x12\x17\n\x0f\x61\x63tivation_code\x18\x01 \x01(\t\x12\x19\n\x11purchase_platform\x18\x02 \x01(\x05\x12\x1e\n\x16is_request_from_client\x18\x03 \x01(\x08\"\x9b\x04\n\x1a\x43Store_PurchaseReceiptInfo\x12\x15\n\rtransactionid\x18\x01 \x01(\x04\x12\x11\n\tpackageid\x18\x02 \x01(\r\x12\x17\n\x0fpurchase_status\x18\x03 \x01(\r\x12\x15\n\rresult_detail\x18\x04 \x01(\r\x12\x18\n\x10transaction_time\x18\x05 \x01(\r\x12\x16\n\x0epayment_method\x18\x06 \x01(\r\x12\x12\n\nbase_price\x18\x07 \x01(\x04\x12\x16\n\x0etotal_discount\x18\x08 \x01(\x04\x12\x0b\n\x03tax\x18\t \x01(\x04\x12\x10\n\x08shipping\x18\n \x01(\x04\x12\x15\n\rcurrency_code\x18\x0b \x01(\r\x12\x14\n\x0c\x63ountry_code\x18\x0c \x01(\t\x12\x16\n\x0e\x65rror_headline\x18\r \x01(\t\x12\x14\n\x0c\x65rror_string\x18\x0e \x01(\t\x12\x17\n\x0f\x65rror_link_text\x18\x0f \x01(\t\x12\x16\n\x0e\x65rror_link_url\x18\x10 \x01(\t\x12\x13\n\x0b\x65rror_appid\x18\x11 \x01(\r\x12\x38\n\nline_items\x18\x12 \x03(\x0b\x32$.CStore_PurchaseReceiptInfo.LineItem\x1aK\n\x08LineItem\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x1d\n\x15line_item_description\x18\x03 \x01(\t\"|\n\x1d\x43Store_RegisterCDKey_Response\x12\x1f\n\x17purchase_result_details\x18\x01 \x01(\x05\x12:\n\x15purchase_receipt_info\x18\x02 \x01(\x0b\x32\x1b.CStore_PurchaseReceiptInfo\"5\n!CStore_GetMostPopularTags_Request\x12\x10\n\x08language\x18\x01 \x01(\t\"\x7f\n\"CStore_GetMostPopularTags_Response\x12\x35\n\x04tags\x18\x01 \x03(\x0b\x32\'.CStore_GetMostPopularTags_Response.Tag\x1a\"\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"J\n&CStore_GetLocalizedNameForTags_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06tagids\x18\x02 \x03(\r\"\xb8\x01\n\'CStore_GetLocalizedNameForTags_Response\x12:\n\x04tags\x18\x01 \x03(\x0b\x32,.CStore_GetLocalizedNameForTags_Response.Tag\x1aQ\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x14\n\x0c\x65nglish_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\x0fnormalized_name\x18\x04 \x01(\t\"H\n\x19\x43Store_GetTagList_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x19\n\x11have_version_hash\x18\x02 \x01(\t\"\x85\x01\n\x1a\x43Store_GetTagList_Response\x12\x14\n\x0cversion_hash\x18\x01 \x01(\t\x12-\n\x04tags\x18\x02 \x03(\x0b\x32\x1f.CStore_GetTagList_Response.Tag\x1a\"\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xe3\x02\n\x1c\x43StoreDiscoveryQueueSettings\x12\x0e\n\x06os_win\x18\x04 \x01(\x08\x12\x0e\n\x06os_mac\x18\x05 \x01(\x08\x12\x10\n\x08os_linux\x18\x06 \x01(\x08\x12\x1f\n\x17\x66ull_controller_support\x18\x07 \x01(\x08\x12\x1f\n\x17native_steam_controller\x18\x08 \x01(\x08\x12\x1b\n\x13include_coming_soon\x18\t \x01(\x08\x12\x17\n\x0f\x65xcluded_tagids\x18\n \x03(\r\x12\x1c\n\x14\x65xclude_early_access\x18\x0b \x01(\x08\x12\x16\n\x0e\x65xclude_videos\x18\x0c \x01(\x08\x12\x18\n\x10\x65xclude_software\x18\r \x01(\x08\x12\x13\n\x0b\x65xclude_dlc\x18\x0e \x01(\x08\x12\x1b\n\x13\x65xclude_soundtracks\x18\x0f \x01(\x08\x12\x17\n\x0f\x66\x65\x61tured_tagids\x18\x10 \x03(\r\"\xb3\x03\n CStore_GetDiscoveryQueue_Request\x12L\n\nqueue_type\x18\x01 \x01(\x0e\x32\x19.EStoreDiscoveryQueueType:\x1dk_EStoreDiscoveryQueueTypeNew\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x15\n\rrebuild_queue\x18\x03 \x01(\x08\x12\x18\n\x10settings_changed\x18\x04 \x01(\x08\x12/\n\x08settings\x18\x05 \x01(\x0b\x32\x1d.CStoreDiscoveryQueueSettings\x12\x1e\n\x16rebuild_queue_if_stale\x18\x06 \x01(\x08\x12\x1f\n\x17ignore_user_preferences\x18\x08 \x01(\x08\x12\x1f\n\x17no_experimental_results\x18\t \x01(\x08\x12\x1b\n\x13\x65xperimental_cohort\x18\n \x01(\r\x12\x1c\n\x14\x64\x65\x62ug_get_solr_query\x18\x0b \x01(\x08\x12,\n\x11store_page_filter\x18\x0c \x01(\x0b\x32\x11.CStorePageFilter\"\xd5\x01\n!CStore_GetDiscoveryQueue_Response\x12\x0e\n\x06\x61ppids\x18\x01 \x03(\r\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12/\n\x08settings\x18\x03 \x01(\x0b\x32\x1d.CStoreDiscoveryQueueSettings\x12\x0f\n\x07skipped\x18\x04 \x01(\x05\x12\x11\n\texhausted\x18\x05 \x01(\x08\x12\x1b\n\x13\x65xperimental_cohort\x18\x06 \x01(\r\x12\x18\n\x10\x64\x65\x62ug_solr_query\x18\x07 \x01(\t\"\xa6\x01\n(CStore_GetDiscoveryQueueSettings_Request\x12L\n\nqueue_type\x18\x01 \x01(\x0e\x32\x19.EStoreDiscoveryQueueType:\x1dk_EStoreDiscoveryQueueTypeNew\x12,\n\x11store_page_filter\x18\x02 \x01(\x0b\x32\x11.CStorePageFilter\"r\n)CStore_GetDiscoveryQueueSettings_Response\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12/\n\x08settings\x18\x02 \x01(\x0b\x32\x1d.CStoreDiscoveryQueueSettings\"\xb2\x01\n%CStore_SkipDiscoveryQueueItem_Request\x12L\n\nqueue_type\x18\x01 \x01(\x0e\x32\x19.EStoreDiscoveryQueueType:\x1dk_EStoreDiscoveryQueueTypeNew\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12,\n\x11store_page_filter\x18\x03 \x01(\x0b\x32\x11.CStorePageFilter\"(\n&CStore_SkipDiscoveryQueueItem_Response\"a\n\'CStore_GetUserGameInterestState_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x13\n\x0bstore_appid\x18\x02 \x01(\r\x12\x12\n\nbeta_appid\x18\x03 \x01(\r\"\xf2\x04\n(CStore_GetUserGameInterestState_Response\x12\r\n\x05owned\x18\x01 \x01(\x08\x12\x10\n\x08wishlist\x18\x02 \x01(\x08\x12\x0f\n\x07ignored\x18\x03 \x01(\x08\x12\x11\n\tfollowing\x18\x04 \x01(\x08\x12,\n\tin_queues\x18\x05 \x03(\x0e\x32\x19.EStoreDiscoveryQueueType\x12\x33\n\x10queues_with_skip\x18\x06 \x03(\x0e\x32\x19.EStoreDiscoveryQueueType\x12\x1d\n\x15queue_items_remaining\x18\x07 \x03(\x05\x12\x1e\n\x16queue_items_next_appid\x18\x08 \x03(\r\x12\x19\n\x11temporarily_owned\x18\t \x01(\x08\x12\x41\n\x06queues\x18\n \x03(\x0b\x32\x31.CStore_GetUserGameInterestState_Response.InQueue\x12\x16\n\x0eignored_reason\x18\x0b \x01(\x05\x12:\n\x0b\x62\x65ta_status\x18\x0c \x01(\x0e\x32\x10.EPlaytestStatus:\x13k_ETesterStatusNone\x1a\xac\x01\n\x07InQueue\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x19.EStoreDiscoveryQueueType:\x1dk_EStoreDiscoveryQueueTypeNew\x12\x0f\n\x07skipped\x18\x02 \x01(\x08\x12\x17\n\x0fitems_remaining\x18\x03 \x01(\x05\x12\x12\n\nnext_appid\x18\x04 \x01(\r\x12\x1b\n\x13\x65xperimental_cohort\x18\x05 \x01(\r\"\xba\x01\n+CStore_GetDiscoveryQueueSkippedApps_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12L\n\nqueue_type\x18\x02 \x01(\x0e\x32\x19.EStoreDiscoveryQueueType:\x1dk_EStoreDiscoveryQueueTypeNew\x12,\n\x11store_page_filter\x18\x03 \x01(\x0b\x32\x11.CStorePageFilter\">\n,CStore_GetDiscoveryQueueSkippedApps_Response\x12\x0e\n\x06\x61ppids\x18\x01 \x03(\r\"y\n\x18\x43Store_ReportApp_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12>\n\x0breport_type\x18\x02 \x01(\x0e\x32\x0f.EAppReportType:\x18k_EAppReportType_Invalid\x12\x0e\n\x06report\x18\x03 \x01(\t\"\x1b\n\x19\x43Store_ReportApp_Response\"$\n\"CStore_GetStorePreferences_Request\"\xf2\x03\n\x16\x43Store_UserPreferences\x12\x18\n\x10primary_language\x18\x01 \x01(\x05\x12\x1b\n\x13secondary_languages\x18\x02 \x01(\r\x12\x18\n\x10platform_windows\x18\x03 \x01(\x08\x12\x14\n\x0cplatform_mac\x18\x04 \x01(\x08\x12\x16\n\x0eplatform_linux\x18\x05 \x01(\x08\x12\x19\n\x11timestamp_updated\x18\x08 \x01(\r\x12\x1c\n\x14hide_store_broadcast\x18\t \x01(\x08\x12`\n\x17review_score_preference\x18\n \x01(\x0e\x32\x1b.EUserReviewScorePreference:\"k_EUserReviewScorePreference_Unset\x12\x38\n0timestamp_content_descriptor_preferences_updated\x18\x0b \x01(\x05\x12\x66\n\x15provide_deck_feedback\x18\x0c \x01(\x0e\x32\x1f.EProvideDeckFeedbackPreference:&k_EProvideDeckFeedbackPreference_Unset\x12\x1c\n\x14\x61\x64\x64itional_languages\x18\r \x01(\t\"\x91\x01\n\x19\x43Store_UserTagPreferences\x12\x37\n\x0ftags_to_exclude\x18\x01 \x03(\x0b\x32\x1e.CStore_UserTagPreferences.Tag\x1a;\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0ftimestamp_added\x18\x03 \x01(\r\"\xd3\x01\n#CStore_GetStorePreferences_Response\x12,\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x17.CStore_UserPreferences\x12\x33\n\x0ftag_preferences\x18\x02 \x01(\x0b\x32\x1a.CStore_UserTagPreferences\x12I\n\x1e\x63ontent_descriptor_preferences\x18\x03 \x01(\x0b\x32!.UserContentDescriptorPreferences\"W\n*CStore_GetTrendingAppsAmongFriends_Request\x12\x10\n\x08num_apps\x18\x01 \x01(\r\x12\x17\n\x0fnum_top_friends\x18\x02 \x01(\r\"\xd9\x01\n+CStore_GetTrendingAppsAmongFriends_Response\x12S\n\rtrending_apps\x18\x01 \x03(\x0b\x32<.CStore_GetTrendingAppsAmongFriends_Response.TrendingAppData\x1aU\n\x0fTrendingAppData\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x1c\n\x14steamids_top_friends\x18\x02 \x03(\x04\x12\x15\n\rtotal_friends\x18\x03 \x01(\r\"\xbf\x01\n.CStore_MigratePartnerLinkTracking_Notification\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x11\n\tbrowserid\x18\x02 \x01(\x04\x12g\n\x0f\x62\x61\x63kfill_source\x18\x03 \x01(\x0e\x32#.EPartnerLinkTrackingBackfillSource:)k_EPartnerLinkTrackingBackfillSource_None\"|\n(CStore_UpdatePackageReservations_Request\x12\x1b\n\x13packages_to_reserve\x18\x01 \x03(\r\x12\x1d\n\x15packages_to_unreserve\x18\x02 \x03(\r\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\"c\n)CStore_UpdatePackageReservations_Response\x12\x36\n\x12reservation_status\x18\x01 \x03(\x0b\x32\x1a.CPackageReservationStatus\"i\n)CStore_GetWishlistDemoEmailStatus_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\ndemo_appid\x18\x02 \x01(\r\x12\x19\n\x11\x61llow_late_firing\x18\x03 \x01(\x08\"u\n*CStore_GetWishlistDemoEmailStatus_Response\x12\x17\n\x08\x63\x61n_fire\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0btime_staged\x18\x02 \x01(\r\x12\x19\n\x11\x64\x65mo_release_date\x18\x03 \x01(\r\"k\n+CStore_QueueWishlistDemoEmailToFire_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\ndemo_appid\x18\x02 \x01(\r\x12\x19\n\x11\x61llow_late_firing\x18\x03 \x01(\x08\".\n,CStore_QueueWishlistDemoEmailToFire_Response\"\xd9\x01\n\x1b\x43ReservationPositionMessage\x12\x14\n\x0c\x65\x64istributor\x18\x01 \x01(\r\x12\x1a\n\x12product_identifier\x18\x02 \x01(\t\x12\x1c\n\x14start_queue_position\x18\x03 \x01(\r\x12$\n\x1crtime_estimated_notification\x18\x04 \x01(\r\x12\x1a\n\x12localization_token\x18\x05 \x01(\t\x12\x11\n\taccountid\x18\x06 \x01(\r\x12\x15\n\rrtime_created\x18\x07 \x01(\r\"^\n,CStore_SetReservationPositionMessage_Request\x12.\n\x08settings\x18\x01 \x03(\x0b\x32\x1c.CReservationPositionMessage\"/\n-CStore_SetReservationPositionMessage_Response\"\x81\x01\n/CStore_DeleteReservationPositionMessage_Request\x12\x14\n\x0c\x65\x64istributor\x18\x01 \x01(\r\x12\x1a\n\x12product_identifier\x18\x02 \x01(\t\x12\x1c\n\x14start_queue_position\x18\x03 \x01(\r\"2\n0CStore_DeleteReservationPositionMessage_Response\"2\n0CStore_GetAllReservationPositionMessages_Request\"c\n1CStore_GetAllReservationPositionMessages_Response\x12.\n\x08settings\x18\x01 \x03(\x0b\x32\x1c.CReservationPositionMessage\":\n8CStore_ReloadAllReservationPositionMessages_Notification\"\x99\x01\n+CSteamDeckCompatibility_SetFeedback_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12[\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x02 \x01(\x0e\x32 .ESteamDeckCompatibilityFeedback:\'k_ESteamDeckCompatibilityFeedback_Unset\".\n,CSteamDeckCompatibility_SetFeedback_Response\"=\n,CSteamDeckCompatibility_ShouldPrompt_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\xc0\x01\n-CSteamDeckCompatibility_ShouldPrompt_Response\x12\x0e\n\x06prompt\x18\x01 \x01(\x08\x12\x19\n\x11\x66\x65\x65\x64\x62\x61\x63k_eligible\x18\x02 \x01(\x08\x12\x64\n\x11\x65xisting_feedback\x18\x03 \x01(\x0e\x32 .ESteamDeckCompatibilityFeedback:\'k_ESteamDeckCompatibilityFeedback_Unset\"\xdb\x01\n+CStore_StorePreferencesChanged_Notification\x12,\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x17.CStore_UserPreferences\x12\x33\n\x0ftag_preferences\x18\x02 \x01(\x0b\x32\x1a.CStore_UserTagPreferences\x12I\n\x1e\x63ontent_descriptor_preferences\x18\x03 \x01(\x0b\x32!.UserContentDescriptorPreferences*\xab\x05\n\x18\x45StoreDiscoveryQueueType\x12!\n\x1dk_EStoreDiscoveryQueueTypeNew\x10\x00\x12(\n$k_EStoreDiscoveryQueueTypeComingSoon\x10\x01\x12)\n%k_EStoreDiscoveryQueueTypeRecommended\x10\x02\x12-\n)k_EStoreDiscoveryQueueTypeEveryNewRelease\x10\x03\x12+\n\'k_EStoreDiscoveryQueueTypeMLRecommender\x10\x05\x12,\n(k_EStoreDiscoveryQueueTypeWishlistOnSale\x10\x06\x12!\n\x1dk_EStoreDiscoveryQueueTypeDLC\x10\x07\x12\'\n#k_EStoreDiscoveryQueueTypeDLCOnSale\x10\x08\x12\x33\n/k_EStoreDiscoveryQueueTypeRecommendedComingSoon\x10\t\x12-\n)k_EStoreDiscoveryQueueTypeRecommendedFree\x10\n\x12/\n+k_EStoreDiscoveryQueueTypeRecommendedOnSale\x10\x0b\x12.\n*k_EStoreDiscoveryQueueTypeRecommendedDemos\x10\x0c\x12,\n(k_EStoreDiscoveryQueueTypeDLCNewReleases\x10\r\x12+\n\'k_EStoreDiscoveryQueueTypeDLCTopSellers\x10\x0e\x12!\n\x1dk_EStoreDiscoveryQueueTypeMAX\x10\x0f*~\n\x0f\x45PlaytestStatus\x12\x17\n\x13k_ETesterStatusNone\x10\x00\x12\x1a\n\x16k_ETesterStatusPending\x10\x01\x12\x1a\n\x16k_ETesterStatusInvited\x10\x02\x12\x1a\n\x16k_ETesterStatusGranted\x10\x03*\xa2\x04\n\x0e\x45\x41ppReportType\x12\x1c\n\x18k_EAppReportType_Invalid\x10\x00\x12\x19\n\x15k_EAppReportType_Scam\x10\x01\x12\x1c\n\x18k_EAppReportType_Malware\x10\x02\x12\x1f\n\x1bk_EAppReportType_HateSpeech\x10\x03\x12 \n\x1ck_EAppReportType_Pornography\x10\x04\x12+\n\'k_EAppReportType_NonLabeledAdultContent\x10\x05\x12\x1d\n\x19k_EAppReportType_Libelous\x10\x06\x12\x1e\n\x1ak_EAppReportType_Offensive\x10\x07\x12%\n!k_EAppReportType_ExploitsChildren\x10\x08\x12\x38\n4k_EAppReportType_MtxWithNonSteamWalletPaymentMethods\x10\t\x12\'\n#k_EAppReportType_CopyrightViolation\x10\n\x12!\n\x1dk_EAppReportType_ViolatesLaws\x10\x0b\x12\x1a\n\x16k_EAppReportType_Other\x10\x0c\x12\x1b\n\x17k_EAppReportType_Broken\x10\r\x12$\n k_EAppReportType_AIContentReport\x10\x0e*\xa0\x01\n\x1a\x45UserReviewScorePreference\x12&\n\"k_EUserReviewScorePreference_Unset\x10\x00\x12+\n\'k_EUserReviewScorePreference_IncludeAll\x10\x01\x12-\n)k_EUserReviewScorePreference_ExcludeBombs\x10\x02*\xe4\x01\n\"EPartnerLinkTrackingBackfillSource\x12-\n)k_EPartnerLinkTrackingBackfillSource_None\x10\x00\x12,\n(k_EPartnerLinkTrackingBackfillSource_Web\x10\x01\x12/\n+k_EPartnerLinkTrackingBackfillSource_Mobile\x10\x02\x12\x30\n,k_EPartnerLinkTrackingBackfillSource_Desktop\x10\x03\x32\x80\x13\n\x05Store\x12N\n\rRegisterCDKey\x12\x1d.CStore_RegisterCDKey_Request\x1a\x1e.CStore_RegisterCDKey_Response\x12]\n\x12GetMostPopularTags\x12\".CStore_GetMostPopularTags_Request\x1a#.CStore_GetMostPopularTags_Response\x12l\n\x17GetLocalizedNameForTags\x12\'.CStore_GetLocalizedNameForTags_Request\x1a(.CStore_GetLocalizedNameForTags_Response\x12\x45\n\nGetTagList\x12\x1a.CStore_GetTagList_Request\x1a\x1b.CStore_GetTagList_Response\x12Z\n\x11GetDiscoveryQueue\x12!.CStore_GetDiscoveryQueue_Request\x1a\".CStore_GetDiscoveryQueue_Response\x12r\n\x19GetDiscoveryQueueSettings\x12).CStore_GetDiscoveryQueueSettings_Request\x1a*.CStore_GetDiscoveryQueueSettings_Response\x12i\n\x16SkipDiscoveryQueueItem\x12&.CStore_SkipDiscoveryQueueItem_Request\x1a\'.CStore_SkipDiscoveryQueueItem_Response\x12o\n\x18GetUserGameInterestState\x12(.CStore_GetUserGameInterestState_Request\x1a).CStore_GetUserGameInterestState_Response\x12{\n\x1cGetDiscoveryQueueSkippedApps\x12,.CStore_GetDiscoveryQueueSkippedApps_Request\x1a-.CStore_GetDiscoveryQueueSkippedApps_Response\x12\x42\n\tReportApp\x12\x19.CStore_ReportApp_Request\x1a\x1a.CStore_ReportApp_Response\x12`\n\x13GetStorePreferences\x12#.CStore_GetStorePreferences_Request\x1a$.CStore_GetStorePreferences_Response\x12x\n\x1bGetTrendingAppsAmongFriends\x12+.CStore_GetTrendingAppsAmongFriends_Request\x1a,.CStore_GetTrendingAppsAmongFriends_Response\x12Z\n\x1aMigratePartnerLinkTracking\x12/.CStore_MigratePartnerLinkTracking_Notification\x1a\x0b.NoResponse\x12r\n\x19UpdatePackageReservations\x12).CStore_UpdatePackageReservations_Request\x1a*.CStore_UpdatePackageReservations_Response\x12u\n\x1aGetWishlistDemoEmailStatus\x12*.CStore_GetWishlistDemoEmailStatus_Request\x1a+.CStore_GetWishlistDemoEmailStatus_Response\x12{\n\x1cQueueWishlistDemoEmailToFire\x12,.CStore_QueueWishlistDemoEmailToFire_Request\x1a-.CStore_QueueWishlistDemoEmailToFire_Response\x12~\n\x1dSetReservationPositionMessage\x12-.CStore_SetReservationPositionMessage_Request\x1a..CStore_SetReservationPositionMessage_Response\x12\x87\x01\n DeleteReservationPositionMessage\x12\x30.CStore_DeleteReservationPositionMessage_Request\x1a\x31.CStore_DeleteReservationPositionMessage_Response\x12\x8a\x01\n!GetAllReservationPositionMessages\x12\x31.CStore_GetAllReservationPositionMessages_Request\x1a\x32.CStore_GetAllReservationPositionMessages_Response\x12n\n$ReloadAllReservationPositionMessages\x12\x39.CStore_ReloadAllReservationPositionMessages_Notification\x1a\x0b.NoResponse\x12w\n\x18SetCompatibilityFeedback\x12,.CSteamDeckCompatibility_SetFeedback_Request\x1a-.CSteamDeckCompatibility_SetFeedback_Response\x12\x85\x01\n$ShouldPromptForCompatibilityFeedback\x12-.CSteamDeckCompatibility_ShouldPrompt_Request\x1a..CSteamDeckCompatibility_ShouldPrompt_Response2o\n\x0bStoreClient\x12Z\n\x1dNotifyStorePreferencesChanged\x12,.CStore_StorePreferencesChanged_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_store_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_STORECLIENT']._options = None
  _globals['_STORECLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_ESTOREDISCOVERYQUEUETYPE']._serialized_start=7676
  _globals['_ESTOREDISCOVERYQUEUETYPE']._serialized_end=8359
  _globals['_EPLAYTESTSTATUS']._serialized_start=8361
  _globals['_EPLAYTESTSTATUS']._serialized_end=8487
  _globals['_EAPPREPORTTYPE']._serialized_start=8490
  _globals['_EAPPREPORTTYPE']._serialized_end=9036
  _globals['_EUSERREVIEWSCOREPREFERENCE']._serialized_start=9039
  _globals['_EUSERREVIEWSCOREPREFERENCE']._serialized_end=9199
  _globals['_EPARTNERLINKTRACKINGBACKFILLSOURCE']._serialized_start=9202
  _globals['_EPARTNERLINKTRACKINGBACKFILLSOURCE']._serialized_end=9430
  _globals['_CSTORE_REGISTERCDKEY_REQUEST']._serialized_start=121
  _globals['_CSTORE_REGISTERCDKEY_REQUEST']._serialized_end=235
  _globals['_CSTORE_PURCHASERECEIPTINFO']._serialized_start=238
  _globals['_CSTORE_PURCHASERECEIPTINFO']._serialized_end=777
  _globals['_CSTORE_PURCHASERECEIPTINFO_LINEITEM']._serialized_start=702
  _globals['_CSTORE_PURCHASERECEIPTINFO_LINEITEM']._serialized_end=777
  _globals['_CSTORE_REGISTERCDKEY_RESPONSE']._serialized_start=779
  _globals['_CSTORE_REGISTERCDKEY_RESPONSE']._serialized_end=903
  _globals['_CSTORE_GETMOSTPOPULARTAGS_REQUEST']._serialized_start=905
  _globals['_CSTORE_GETMOSTPOPULARTAGS_REQUEST']._serialized_end=958
  _globals['_CSTORE_GETMOSTPOPULARTAGS_RESPONSE']._serialized_start=960
  _globals['_CSTORE_GETMOSTPOPULARTAGS_RESPONSE']._serialized_end=1087
  _globals['_CSTORE_GETMOSTPOPULARTAGS_RESPONSE_TAG']._serialized_start=1053
  _globals['_CSTORE_GETMOSTPOPULARTAGS_RESPONSE_TAG']._serialized_end=1087
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST']._serialized_start=1089
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST']._serialized_end=1163
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE']._serialized_start=1166
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE']._serialized_end=1350
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG']._serialized_start=1269
  _globals['_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG']._serialized_end=1350
  _globals['_CSTORE_GETTAGLIST_REQUEST']._serialized_start=1352
  _globals['_CSTORE_GETTAGLIST_REQUEST']._serialized_end=1424
  _globals['_CSTORE_GETTAGLIST_RESPONSE']._serialized_start=1427
  _globals['_CSTORE_GETTAGLIST_RESPONSE']._serialized_end=1560
  _globals['_CSTORE_GETTAGLIST_RESPONSE_TAG']._serialized_start=1053
  _globals['_CSTORE_GETTAGLIST_RESPONSE_TAG']._serialized_end=1087
  _globals['_CSTOREDISCOVERYQUEUESETTINGS']._serialized_start=1563
  _globals['_CSTOREDISCOVERYQUEUESETTINGS']._serialized_end=1918
  _globals['_CSTORE_GETDISCOVERYQUEUE_REQUEST']._serialized_start=1921
  _globals['_CSTORE_GETDISCOVERYQUEUE_REQUEST']._serialized_end=2356
  _globals['_CSTORE_GETDISCOVERYQUEUE_RESPONSE']._serialized_start=2359
  _globals['_CSTORE_GETDISCOVERYQUEUE_RESPONSE']._serialized_end=2572
  _globals['_CSTORE_GETDISCOVERYQUEUESETTINGS_REQUEST']._serialized_start=2575
  _globals['_CSTORE_GETDISCOVERYQUEUESETTINGS_REQUEST']._serialized_end=2741
  _globals['_CSTORE_GETDISCOVERYQUEUESETTINGS_RESPONSE']._serialized_start=2743
  _globals['_CSTORE_GETDISCOVERYQUEUESETTINGS_RESPONSE']._serialized_end=2857
  _globals['_CSTORE_SKIPDISCOVERYQUEUEITEM_REQUEST']._serialized_start=2860
  _globals['_CSTORE_SKIPDISCOVERYQUEUEITEM_REQUEST']._serialized_end=3038
  _globals['_CSTORE_SKIPDISCOVERYQUEUEITEM_RESPONSE']._serialized_start=3040
  _globals['_CSTORE_SKIPDISCOVERYQUEUEITEM_RESPONSE']._serialized_end=3080
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_REQUEST']._serialized_start=3082
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_REQUEST']._serialized_end=3179
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_RESPONSE']._serialized_start=3182
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_RESPONSE']._serialized_end=3808
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_RESPONSE_INQUEUE']._serialized_start=3636
  _globals['_CSTORE_GETUSERGAMEINTERESTSTATE_RESPONSE_INQUEUE']._serialized_end=3808
  _globals['_CSTORE_GETDISCOVERYQUEUESKIPPEDAPPS_REQUEST']._serialized_start=3811
  _globals['_CSTORE_GETDISCOVERYQUEUESKIPPEDAPPS_REQUEST']._serialized_end=3997
  _globals['_CSTORE_GETDISCOVERYQUEUESKIPPEDAPPS_RESPONSE']._serialized_start=3999
  _globals['_CSTORE_GETDISCOVERYQUEUESKIPPEDAPPS_RESPONSE']._serialized_end=4061
  _globals['_CSTORE_REPORTAPP_REQUEST']._serialized_start=4063
  _globals['_CSTORE_REPORTAPP_REQUEST']._serialized_end=4184
  _globals['_CSTORE_REPORTAPP_RESPONSE']._serialized_start=4186
  _globals['_CSTORE_REPORTAPP_RESPONSE']._serialized_end=4213
  _globals['_CSTORE_GETSTOREPREFERENCES_REQUEST']._serialized_start=4215
  _globals['_CSTORE_GETSTOREPREFERENCES_REQUEST']._serialized_end=4251
  _globals['_CSTORE_USERPREFERENCES']._serialized_start=4254
  _globals['_CSTORE_USERPREFERENCES']._serialized_end=4752
  _globals['_CSTORE_USERTAGPREFERENCES']._serialized_start=4755
  _globals['_CSTORE_USERTAGPREFERENCES']._serialized_end=4900
  _globals['_CSTORE_USERTAGPREFERENCES_TAG']._serialized_start=4841
  _globals['_CSTORE_USERTAGPREFERENCES_TAG']._serialized_end=4900
  _globals['_CSTORE_GETSTOREPREFERENCES_RESPONSE']._serialized_start=4903
  _globals['_CSTORE_GETSTOREPREFERENCES_RESPONSE']._serialized_end=5114
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_REQUEST']._serialized_start=5116
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_REQUEST']._serialized_end=5203
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_RESPONSE']._serialized_start=5206
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_RESPONSE']._serialized_end=5423
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_RESPONSE_TRENDINGAPPDATA']._serialized_start=5338
  _globals['_CSTORE_GETTRENDINGAPPSAMONGFRIENDS_RESPONSE_TRENDINGAPPDATA']._serialized_end=5423
  _globals['_CSTORE_MIGRATEPARTNERLINKTRACKING_NOTIFICATION']._serialized_start=5426
  _globals['_CSTORE_MIGRATEPARTNERLINKTRACKING_NOTIFICATION']._serialized_end=5617
  _globals['_CSTORE_UPDATEPACKAGERESERVATIONS_REQUEST']._serialized_start=5619
  _globals['_CSTORE_UPDATEPACKAGERESERVATIONS_REQUEST']._serialized_end=5743
  _globals['_CSTORE_UPDATEPACKAGERESERVATIONS_RESPONSE']._serialized_start=5745
  _globals['_CSTORE_UPDATEPACKAGERESERVATIONS_RESPONSE']._serialized_end=5844
  _globals['_CSTORE_GETWISHLISTDEMOEMAILSTATUS_REQUEST']._serialized_start=5846
  _globals['_CSTORE_GETWISHLISTDEMOEMAILSTATUS_REQUEST']._serialized_end=5951
  _globals['_CSTORE_GETWISHLISTDEMOEMAILSTATUS_RESPONSE']._serialized_start=5953
  _globals['_CSTORE_GETWISHLISTDEMOEMAILSTATUS_RESPONSE']._serialized_end=6070
  _globals['_CSTORE_QUEUEWISHLISTDEMOEMAILTOFIRE_REQUEST']._serialized_start=6072
  _globals['_CSTORE_QUEUEWISHLISTDEMOEMAILTOFIRE_REQUEST']._serialized_end=6179
  _globals['_CSTORE_QUEUEWISHLISTDEMOEMAILTOFIRE_RESPONSE']._serialized_start=6181
  _globals['_CSTORE_QUEUEWISHLISTDEMOEMAILTOFIRE_RESPONSE']._serialized_end=6227
  _globals['_CRESERVATIONPOSITIONMESSAGE']._serialized_start=6230
  _globals['_CRESERVATIONPOSITIONMESSAGE']._serialized_end=6447
  _globals['_CSTORE_SETRESERVATIONPOSITIONMESSAGE_REQUEST']._serialized_start=6449
  _globals['_CSTORE_SETRESERVATIONPOSITIONMESSAGE_REQUEST']._serialized_end=6543
  _globals['_CSTORE_SETRESERVATIONPOSITIONMESSAGE_RESPONSE']._serialized_start=6545
  _globals['_CSTORE_SETRESERVATIONPOSITIONMESSAGE_RESPONSE']._serialized_end=6592
  _globals['_CSTORE_DELETERESERVATIONPOSITIONMESSAGE_REQUEST']._serialized_start=6595
  _globals['_CSTORE_DELETERESERVATIONPOSITIONMESSAGE_REQUEST']._serialized_end=6724
  _globals['_CSTORE_DELETERESERVATIONPOSITIONMESSAGE_RESPONSE']._serialized_start=6726
  _globals['_CSTORE_DELETERESERVATIONPOSITIONMESSAGE_RESPONSE']._serialized_end=6776
  _globals['_CSTORE_GETALLRESERVATIONPOSITIONMESSAGES_REQUEST']._serialized_start=6778
  _globals['_CSTORE_GETALLRESERVATIONPOSITIONMESSAGES_REQUEST']._serialized_end=6828
  _globals['_CSTORE_GETALLRESERVATIONPOSITIONMESSAGES_RESPONSE']._serialized_start=6830
  _globals['_CSTORE_GETALLRESERVATIONPOSITIONMESSAGES_RESPONSE']._serialized_end=6929
  _globals['_CSTORE_RELOADALLRESERVATIONPOSITIONMESSAGES_NOTIFICATION']._serialized_start=6931
  _globals['_CSTORE_RELOADALLRESERVATIONPOSITIONMESSAGES_NOTIFICATION']._serialized_end=6989
  _globals['_CSTEAMDECKCOMPATIBILITY_SETFEEDBACK_REQUEST']._serialized_start=6992
  _globals['_CSTEAMDECKCOMPATIBILITY_SETFEEDBACK_REQUEST']._serialized_end=7145
  _globals['_CSTEAMDECKCOMPATIBILITY_SETFEEDBACK_RESPONSE']._serialized_start=7147
  _globals['_CSTEAMDECKCOMPATIBILITY_SETFEEDBACK_RESPONSE']._serialized_end=7193
  _globals['_CSTEAMDECKCOMPATIBILITY_SHOULDPROMPT_REQUEST']._serialized_start=7195
  _globals['_CSTEAMDECKCOMPATIBILITY_SHOULDPROMPT_REQUEST']._serialized_end=7256
  _globals['_CSTEAMDECKCOMPATIBILITY_SHOULDPROMPT_RESPONSE']._serialized_start=7259
  _globals['_CSTEAMDECKCOMPATIBILITY_SHOULDPROMPT_RESPONSE']._serialized_end=7451
  _globals['_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION']._serialized_start=7454
  _globals['_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION']._serialized_end=7673
  _globals['_STORE']._serialized_start=9433
  _globals['_STORE']._serialized_end=11865
  _globals['_STORECLIENT']._serialized_start=11867
  _globals['_STORECLIENT']._serialized_end=11978
_builder.BuildServices(DESCRIPTOR, 'steammessages_store_pb2', _globals)
# @@protoc_insertion_point(module_scope)
