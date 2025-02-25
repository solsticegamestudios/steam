# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.encrypted_app_ticket_pb2 as encrypted__app__ticket__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steammessages_clientserver.proto\x1a\x18steammessages_base.proto\x1a\x1a\x65ncrypted_app_ticket.proto\"j\n\"CMsgClientRegisterAuthTicketWithCM\x12\x18\n\x10protocol_version\x18\x01 \x01(\r\x12\x0e\n\x06ticket\x18\x03 \x01(\x0c\x12\x1a\n\x12\x63lient_instance_id\x18\x04 \x01(\x04\"\xd1\x01\n\x1c\x43MsgClientTicketAuthComplete\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\x12\x0e\n\x06\x65state\x18\x03 \x01(\r\x12\x1e\n\x16\x65\x61uth_session_response\x18\x04 \x01(\r\x12\x19\n\x11\x44\x45PRECATED_ticket\x18\x05 \x01(\x0c\x12\x12\n\nticket_crc\x18\x06 \x01(\r\x12\x17\n\x0fticket_sequence\x18\x07 \x01(\r\x12\x16\n\x0eowner_steam_id\x18\x08 \x01(\x06\"\xa3\x01\n\x1b\x43MsgClientP2PConnectionInfo\x12\x15\n\rsteam_id_dest\x18\x01 \x01(\x06\x12\x14\n\x0csteam_id_src\x18\x02 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\x12\x11\n\tcandidate\x18\x04 \x01(\x0c\x12 \n\x18legacy_connection_id_src\x18\x05 \x01(\x06\x12\x12\n\nrendezvous\x18\x06 \x01(\x0c\"\xc3\x01\n\x1f\x43MsgClientP2PConnectionFailInfo\x12\x15\n\rsteam_id_dest\x18\x01 \x01(\x06\x12\x14\n\x0csteam_id_src\x18\x02 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\x12\x1a\n\x12\x65p2p_session_error\x18\x04 \x01(\r\x12\x1a\n\x12\x63onnection_id_dest\x18\x05 \x01(\x06\x12\x14\n\x0c\x63lose_reason\x18\x07 \x01(\r\x12\x15\n\rclose_message\x18\x08 \x01(\t\"C\n\x1f\x43MsgClientNetworkingCertRequest\x12\x10\n\x08key_data\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\"V\n\x1d\x43MsgClientNetworkingCertReply\x12\x0c\n\x04\x63\x65rt\x18\x04 \x01(\x0c\x12\x11\n\tca_key_id\x18\x05 \x01(\x06\x12\x14\n\x0c\x63\x61_signature\x18\x06 \x01(\x0c\"7\n%CMsgClientNetworkingMobileCertRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\";\n#CMsgClientNetworkingMobileCertReply\x12\x14\n\x0c\x65ncoded_cert\x18\x01 \x01(\t\"1\n\x1f\x43MsgClientGetAppOwnershipTicket\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\"]\n\'CMsgClientGetAppOwnershipTicketResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\r:\x01\x32\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x0e\n\x06ticket\x18\x03 \x01(\x0c\"\'\n\x16\x43MsgClientSessionToken\x12\r\n\x05token\x18\x01 \x01(\x04\"M\n\x1b\x43MsgClientGameConnectTokens\x12\x1e\n\x12max_tokens_to_keep\x18\x01 \x01(\r:\x02\x31\x30\x12\x0e\n\x06tokens\x18\x02 \x03(\x0c\"\x99\t\n\x15\x43MsgClientGamesPlayed\x12\x37\n\x0cgames_played\x18\x01 \x03(\x0b\x32!.CMsgClientGamesPlayed.GamePlayed\x12\x16\n\x0e\x63lient_os_type\x18\x02 \x01(\r\x12\x1d\n\x15\x63loud_gaming_platform\x18\x03 \x01(\r\x12\x1f\n\x17recent_reauthentication\x18\x04 \x01(\x08\x1aU\n\x0bProcessInfo\x12\x12\n\nprocess_id\x18\x01 \x01(\r\x12\x19\n\x11process_id_parent\x18\x02 \x01(\r\x12\x17\n\x0fparent_is_steam\x18\x03 \x01(\x08\x1a\x97\x07\n\nGamePlayed\x12\x13\n\x0bsteam_id_gs\x18\x01 \x01(\x04\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\x12\"\n\x1a\x64\x65precated_game_ip_address\x18\x03 \x01(\r\x12\x11\n\tgame_port\x18\x04 \x01(\r\x12\x11\n\tis_secure\x18\x05 \x01(\x08\x12\r\n\x05token\x18\x06 \x01(\x0c\x12\x17\n\x0fgame_extra_info\x18\x07 \x01(\t\x12\x16\n\x0egame_data_blob\x18\x08 \x01(\x0c\x12\x12\n\nprocess_id\x18\t \x01(\r\x12\x1d\n\x15streaming_provider_id\x18\n \x01(\r\x12\x12\n\ngame_flags\x18\x0b \x01(\r\x12\x10\n\x08owner_id\x18\x0c \x01(\r\x12\x15\n\rvr_hmd_vendor\x18\r \x01(\t\x12\x14\n\x0cvr_hmd_model\x18\x0e \x01(\t\x12\x1d\n\x12launch_option_type\x18\x0f \x01(\r:\x01\x30\x12#\n\x17primary_controller_type\x18\x10 \x01(\x05:\x02-1\x12\'\n\x1fprimary_steam_controller_serial\x18\x11 \x01(\t\x12\'\n\x1ctotal_steam_controller_count\x18\x12 \x01(\r:\x01\x30\x12+\n total_non_steam_controller_count\x18\x13 \x01(\r:\x01\x30\x12&\n\x1b\x63ontroller_workshop_file_id\x18\x14 \x01(\x04:\x01\x30\x12\x18\n\rlaunch_source\x18\x15 \x01(\r:\x01\x30\x12\x16\n\x0evr_hmd_runtime\x18\x16 \x01(\r\x12\'\n\x0fgame_ip_address\x18\x17 \x01(\x0b\x32\x0e.CMsgIPAddress\x12%\n\x1a\x63ontroller_connection_type\x18\x18 \x01(\r:\x01\x30\x12\x18\n\x10game_os_platform\x18\x19 \x01(\x05\x12\x15\n\rgame_build_id\x18\x1a \x01(\r\x12\x19\n\x0e\x63ompat_tool_id\x18\x1b \x01(\r:\x01\x30\x12\x17\n\x0f\x63ompat_tool_cmd\x18\x1c \x01(\t\x12\x1c\n\x14\x63ompat_tool_build_id\x18\x1d \x01(\r\x12\x11\n\tbeta_name\x18\x1e \x01(\t\x12\x13\n\x0b\x64lc_context\x18\x1f \x01(\r\x12;\n\x0fprocess_id_list\x18  \x03(\x0b\x32\".CMsgClientGamesPlayed.ProcessInfo\"9\n\rCMsgGSApprove\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x16\n\x0eowner_steam_id\x18\x02 \x01(\x06\"I\n\nCMsgGSDeny\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x14\n\x0c\x65\x64\x65ny_reason\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65ny_string\x18\x03 \x01(\t\"4\n\nCMsgGSKick\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x14\n\x0c\x65\x64\x65ny_reason\x18\x02 \x01(\x05\"\xc8\x01\n\x12\x43MsgClientAuthList\x12\x13\n\x0btokens_left\x18\x01 \x01(\r\x12\x18\n\x10last_request_seq\x18\x02 \x01(\r\x12$\n\x1clast_request_seq_from_server\x18\x03 \x01(\r\x12 \n\x07tickets\x18\x04 \x03(\x0b\x32\x0f.CMsgAuthTicket\x12\x0f\n\x07\x61pp_ids\x18\x05 \x03(\r\x12\x18\n\x10message_sequence\x18\x06 \x01(\r\x12\x10\n\x08\x66iltered\x18\x07 \x01(\x08\"V\n\x15\x43MsgClientAuthListAck\x12\x12\n\nticket_crc\x18\x01 \x03(\r\x12\x0f\n\x07\x61pp_ids\x18\x02 \x03(\r\x12\x18\n\x10message_sequence\x18\x03 \x01(\r\"\x8e\x04\n\x15\x43MsgClientLicenseList\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x30\n\x08licenses\x18\x02 \x03(\x0b\x32\x1e.CMsgClientLicenseList.License\x1a\xae\x03\n\x07License\x12\x12\n\npackage_id\x18\x01 \x01(\r\x12\x14\n\x0ctime_created\x18\x02 \x01(\x07\x12\x19\n\x11time_next_process\x18\x03 \x01(\x07\x12\x14\n\x0cminute_limit\x18\x04 \x01(\x05\x12\x14\n\x0cminutes_used\x18\x05 \x01(\x05\x12\x16\n\x0epayment_method\x18\x06 \x01(\r\x12\r\n\x05\x66lags\x18\x07 \x01(\r\x12\x1d\n\x15purchase_country_code\x18\x08 \x01(\t\x12\x14\n\x0clicense_type\x18\t \x01(\r\x12\x16\n\x0eterritory_code\x18\n \x01(\x05\x12\x15\n\rchange_number\x18\x0b \x01(\x05\x12\x10\n\x08owner_id\x18\x0c \x01(\r\x12\x16\n\x0einitial_period\x18\r \x01(\r\x12\x19\n\x11initial_time_unit\x18\x0e \x01(\r\x12\x16\n\x0erenewal_period\x18\x0f \x01(\r\x12\x19\n\x11renewal_time_unit\x18\x10 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x11 \x01(\x04\x12\x19\n\x11master_package_id\x18\x12 \x01(\r\"\xaa\x01\n\x1a\x43MsgClientIsLimitedAccount\x12\x1b\n\x13\x62is_limited_account\x18\x01 \x01(\x08\x12\x1c\n\x14\x62is_community_banned\x18\x02 \x01(\x08\x12\x1a\n\x12\x62is_locked_account\x18\x03 \x01(\x08\x12\x35\n-bis_limited_account_allowed_to_invite_friends\x18\x04 \x01(\x08\"\xa7\x01\n\x1e\x43MsgClientRequestedClientStats\x12\x42\n\rstats_to_send\x18\x01 \x03(\x0b\x32+.CMsgClientRequestedClientStats.StatsToSend\x1a\x41\n\x0bStatsToSend\x12\x13\n\x0b\x63lient_stat\x18\x01 \x01(\r\x12\x1d\n\x15stat_aggregate_method\x18\x02 \x01(\r\"\xc0\x01\n\x0f\x43MsgClientStat2\x12\x30\n\x0bstat_detail\x18\x01 \x03(\x0b\x32\x1b.CMsgClientStat2.StatDetail\x1a{\n\nStatDetail\x12\x13\n\x0b\x63lient_stat\x18\x01 \x01(\r\x12\x10\n\x08ll_value\x18\x02 \x01(\x03\x12\x13\n\x0btime_of_day\x18\x03 \x01(\r\x12\x0f\n\x07\x63\x65ll_id\x18\x04 \x01(\r\x12\x10\n\x08\x64\x65pot_id\x18\x05 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x06 \x01(\r\"r\n\x16\x43MsgClientInviteToGame\x12\x15\n\rsteam_id_dest\x18\x01 \x01(\x06\x12\x14\n\x0csteam_id_src\x18\x02 \x01(\x06\x12\x16\n\x0e\x63onnect_string\x18\x03 \x01(\t\x12\x13\n\x0bremote_play\x18\x04 \x01(\t\"\xb9\x01\n\x14\x43MsgClientChatInvite\x12\x18\n\x10steam_id_invited\x18\x01 \x01(\x06\x12\x15\n\rsteam_id_chat\x18\x02 \x01(\x06\x12\x17\n\x0fsteam_id_patron\x18\x03 \x01(\x06\x12\x15\n\rchatroom_type\x18\x04 \x01(\x05\x12\x1c\n\x14steam_id_friend_chat\x18\x05 \x01(\x06\x12\x11\n\tchat_name\x18\x06 \x01(\t\x12\x0f\n\x07game_id\x18\x07 \x01(\x06\"\xf9\x08\n\x19\x43MsgClientConnectionStats\x12;\n\x0bstats_logon\x18\x01 \x01(\x0b\x32&.CMsgClientConnectionStats.Stats_Logon\x12;\n\x0bstats_vconn\x18\x02 \x01(\x0b\x32&.CMsgClientConnectionStats.Stats_VConn\x1a\xd3\x02\n\x0bStats_Logon\x12\x18\n\x10\x63onnect_attempts\x18\x01 \x01(\x05\x12\x19\n\x11\x63onnect_successes\x18\x02 \x01(\x05\x12\x18\n\x10\x63onnect_failures\x18\x03 \x01(\x05\x12\x1b\n\x13\x63onnections_dropped\x18\x04 \x01(\x05\x12\x17\n\x0fseconds_running\x18\x05 \x01(\r\x12\x1c\n\x14msec_tologonthistime\x18\x06 \x01(\r\x12\x15\n\rcount_bad_cms\x18\x07 \x01(\r\x12\x1b\n\x13no_udp_connectivity\x18\x08 \x01(\x08\x12\x1b\n\x13no_tcp_connectivity\x18\t \x01(\x08\x12%\n\x1dno_websocket_443_connectivity\x18\n \x01(\x08\x12)\n!no_websocket_non_443_connectivity\x18\x0b \x01(\x08\x1aq\n\tStats_UDP\x12\x11\n\tpkts_sent\x18\x01 \x01(\x04\x12\x12\n\nbytes_sent\x18\x02 \x01(\x04\x12\x11\n\tpkts_recv\x18\x03 \x01(\x04\x12\x16\n\x0epkts_processed\x18\x04 \x01(\x04\x12\x12\n\nbytes_recv\x18\x05 \x01(\x04\x1a\x98\x04\n\x0bStats_VConn\x12\x17\n\x0f\x63onnections_udp\x18\x01 \x01(\r\x12\x17\n\x0f\x63onnections_tcp\x18\x02 \x01(\r\x12\x37\n\tstats_udp\x18\x03 \x01(\x0b\x32$.CMsgClientConnectionStats.Stats_UDP\x12\x16\n\x0epkts_abandoned\x18\x04 \x01(\x04\x12\x19\n\x11\x63onn_req_received\x18\x05 \x01(\x04\x12\x13\n\x0bpkts_resent\x18\x06 \x01(\x04\x12\x11\n\tmsgs_sent\x18\x07 \x01(\x04\x12\x18\n\x10msgs_sent_failed\x18\x08 \x01(\x04\x12\x11\n\tmsgs_recv\x18\t \x01(\x04\x12\x16\n\x0e\x64\x61tagrams_sent\x18\n \x01(\x04\x12\x16\n\x0e\x64\x61tagrams_recv\x18\x0b \x01(\x04\x12\x15\n\rbad_pkts_recv\x18\x0c \x01(\x04\x12\x1e\n\x16unknown_conn_pkts_recv\x18\r \x01(\x04\x12\x18\n\x10missed_pkts_recv\x18\x0e \x01(\x04\x12\x15\n\rdup_pkts_recv\x18\x0f \x01(\x04\x12!\n\x19\x66\x61iled_connect_challenges\x18\x10 \x01(\x04\x12\x1d\n\x15micro_sec_avg_latency\x18\x11 \x01(\r\x12\x1d\n\x15micro_sec_min_latency\x18\x12 \x01(\r\x12\x1d\n\x15micro_sec_max_latency\x18\x13 \x01(\r\"\xd2\x01\n\x1a\x43MsgClientServersAvailable\x12R\n\x16server_types_available\x18\x01 \x03(\x0b\x32\x32.CMsgClientServersAvailable.Server_Types_Available\x12%\n\x1dserver_type_for_auth_services\x18\x02 \x01(\r\x1a\x39\n\x16Server_Types_Available\x12\x0e\n\x06server\x18\x01 \x01(\r\x12\x0f\n\x07\x63hanged\x18\x02 \x01(\x08\"?\n$CMsgClientReportOverlayDetourFailure\x12\x17\n\x0f\x66\x61ilure_strings\x18\x01 \x03(\t\"G\n#CMsgClientRequestEncryptedAppTicket\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x10\n\x08userdata\x18\x02 \x01(\x0c\"\x84\x01\n+CMsgClientRequestEncryptedAppTicketResponse\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x12\n\x07\x65result\x18\x02 \x01(\x05:\x01\x32\x12\x31\n\x14\x65ncrypted_app_ticket\x18\x03 \x01(\x0b\x32\x13.EncryptedAppTicket\"\xb5\x01\n\x1a\x43MsgClientWalletInfoUpdate\x12\x12\n\nhas_wallet\x18\x01 \x01(\x08\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x05\x12\x10\n\x08\x63urrency\x18\x03 \x01(\x05\x12\x17\n\x0f\x62\x61lance_delayed\x18\x04 \x01(\x05\x12\x17\n\tbalance64\x18\x05 \x01(\x03\x42\x04\xa0\xb6\x18\x01\x12\x1f\n\x11\x62\x61lance64_delayed\x18\x06 \x01(\x03\x42\x04\xa0\xb6\x18\x01\x12\r\n\x05realm\x18\x07 \x01(\x05\"3\n\x1b\x43MsgClientAMGetClanOfficers\x12\x14\n\x0csteamid_clan\x18\x01 \x01(\x06\"f\n#CMsgClientAMGetClanOfficersResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x14\n\x0csteamid_clan\x18\x02 \x01(\x06\x12\x15\n\rofficer_count\x18\x03 \x01(\x05\"\x90\x01\n!CMsgClientAMGetPersonaNameHistory\x12\x10\n\x08id_count\x18\x01 \x01(\x05\x12:\n\x03Ids\x18\x02 \x03(\x0b\x32-.CMsgClientAMGetPersonaNameHistory.IdInstance\x1a\x1d\n\nIdInstance\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xc3\x02\n)CMsgClientAMGetPersonaNameHistoryResponse\x12O\n\tresponses\x18\x02 \x03(\x0b\x32<.CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance\x1a\xc4\x01\n\x11NameTableInstance\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12X\n\x05names\x18\x03 \x03(\x0b\x32I.CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance.NameInstance\x1a\x30\n\x0cNameInstance\x12\x12\n\nname_since\x18\x01 \x01(\x07\x12\x0c\n\x04name\x18\x02 \x01(\t\"E\n\x1e\x43MsgClientDeregisterWithServer\x12\x13\n\x0b\x65servertype\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\"\xab\x04\n\x13\x43MsgClientClanState\x12\x14\n\x0csteamid_clan\x18\x01 \x01(\x06\x12\x1a\n\x12\x63lan_account_flags\x18\x03 \x01(\r\x12\x30\n\tname_info\x18\x04 \x01(\x0b\x32\x1d.CMsgClientClanState.NameInfo\x12\x34\n\x0buser_counts\x18\x05 \x01(\x0b\x32\x1f.CMsgClientClanState.UserCounts\x12*\n\x06\x65vents\x18\x06 \x03(\x0b\x32\x1a.CMsgClientClanState.Event\x12\x31\n\rannouncements\x18\x07 \x03(\x0b\x32\x1a.CMsgClientClanState.Event\x12\x19\n\x11\x63hat_room_private\x18\x08 \x01(\x08\x1a\x31\n\x08NameInfo\x12\x11\n\tclan_name\x18\x01 \x01(\t\x12\x12\n\nsha_avatar\x18\x02 \x01(\x0c\x1ak\n\nUserCounts\x12\x0f\n\x07members\x18\x01 \x01(\r\x12\x0e\n\x06online\x18\x02 \x01(\r\x12\x10\n\x08\x63hatting\x18\x03 \x01(\r\x12\x0f\n\x07in_game\x18\x04 \x01(\r\x12\x19\n\x11\x63hat_room_members\x18\x05 \x01(\r\x1a`\n\x05\x45vent\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\x12\n\nevent_time\x18\x02 \x01(\r\x12\x10\n\x08headline\x18\x03 \x01(\t\x12\x0f\n\x07game_id\x18\x04 \x01(\x06\x12\x13\n\x0bjust_posted\x18\x05 \x01(\x08\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTWALLETINFOUPDATE'].fields_by_name['balance64']._options = None
  _globals['_CMSGCLIENTWALLETINFOUPDATE'].fields_by_name['balance64']._serialized_options = b'\240\266\030\001'
  _globals['_CMSGCLIENTWALLETINFOUPDATE'].fields_by_name['balance64_delayed']._options = None
  _globals['_CMSGCLIENTWALLETINFOUPDATE'].fields_by_name['balance64_delayed']._serialized_options = b'\240\266\030\001'
  _globals['_CMSGCLIENTREGISTERAUTHTICKETWITHCM']._serialized_start=90
  _globals['_CMSGCLIENTREGISTERAUTHTICKETWITHCM']._serialized_end=196
  _globals['_CMSGCLIENTTICKETAUTHCOMPLETE']._serialized_start=199
  _globals['_CMSGCLIENTTICKETAUTHCOMPLETE']._serialized_end=408
  _globals['_CMSGCLIENTP2PCONNECTIONINFO']._serialized_start=411
  _globals['_CMSGCLIENTP2PCONNECTIONINFO']._serialized_end=574
  _globals['_CMSGCLIENTP2PCONNECTIONFAILINFO']._serialized_start=577
  _globals['_CMSGCLIENTP2PCONNECTIONFAILINFO']._serialized_end=772
  _globals['_CMSGCLIENTNETWORKINGCERTREQUEST']._serialized_start=774
  _globals['_CMSGCLIENTNETWORKINGCERTREQUEST']._serialized_end=841
  _globals['_CMSGCLIENTNETWORKINGCERTREPLY']._serialized_start=843
  _globals['_CMSGCLIENTNETWORKINGCERTREPLY']._serialized_end=929
  _globals['_CMSGCLIENTNETWORKINGMOBILECERTREQUEST']._serialized_start=931
  _globals['_CMSGCLIENTNETWORKINGMOBILECERTREQUEST']._serialized_end=986
  _globals['_CMSGCLIENTNETWORKINGMOBILECERTREPLY']._serialized_start=988
  _globals['_CMSGCLIENTNETWORKINGMOBILECERTREPLY']._serialized_end=1047
  _globals['_CMSGCLIENTGETAPPOWNERSHIPTICKET']._serialized_start=1049
  _globals['_CMSGCLIENTGETAPPOWNERSHIPTICKET']._serialized_end=1098
  _globals['_CMSGCLIENTGETAPPOWNERSHIPTICKETRESPONSE']._serialized_start=1100
  _globals['_CMSGCLIENTGETAPPOWNERSHIPTICKETRESPONSE']._serialized_end=1193
  _globals['_CMSGCLIENTSESSIONTOKEN']._serialized_start=1195
  _globals['_CMSGCLIENTSESSIONTOKEN']._serialized_end=1234
  _globals['_CMSGCLIENTGAMECONNECTTOKENS']._serialized_start=1236
  _globals['_CMSGCLIENTGAMECONNECTTOKENS']._serialized_end=1313
  _globals['_CMSGCLIENTGAMESPLAYED']._serialized_start=1316
  _globals['_CMSGCLIENTGAMESPLAYED']._serialized_end=2493
  _globals['_CMSGCLIENTGAMESPLAYED_PROCESSINFO']._serialized_start=1486
  _globals['_CMSGCLIENTGAMESPLAYED_PROCESSINFO']._serialized_end=1571
  _globals['_CMSGCLIENTGAMESPLAYED_GAMEPLAYED']._serialized_start=1574
  _globals['_CMSGCLIENTGAMESPLAYED_GAMEPLAYED']._serialized_end=2493
  _globals['_CMSGGSAPPROVE']._serialized_start=2495
  _globals['_CMSGGSAPPROVE']._serialized_end=2552
  _globals['_CMSGGSDENY']._serialized_start=2554
  _globals['_CMSGGSDENY']._serialized_end=2627
  _globals['_CMSGGSKICK']._serialized_start=2629
  _globals['_CMSGGSKICK']._serialized_end=2681
  _globals['_CMSGCLIENTAUTHLIST']._serialized_start=2684
  _globals['_CMSGCLIENTAUTHLIST']._serialized_end=2884
  _globals['_CMSGCLIENTAUTHLISTACK']._serialized_start=2886
  _globals['_CMSGCLIENTAUTHLISTACK']._serialized_end=2972
  _globals['_CMSGCLIENTLICENSELIST']._serialized_start=2975
  _globals['_CMSGCLIENTLICENSELIST']._serialized_end=3501
  _globals['_CMSGCLIENTLICENSELIST_LICENSE']._serialized_start=3071
  _globals['_CMSGCLIENTLICENSELIST_LICENSE']._serialized_end=3501
  _globals['_CMSGCLIENTISLIMITEDACCOUNT']._serialized_start=3504
  _globals['_CMSGCLIENTISLIMITEDACCOUNT']._serialized_end=3674
  _globals['_CMSGCLIENTREQUESTEDCLIENTSTATS']._serialized_start=3677
  _globals['_CMSGCLIENTREQUESTEDCLIENTSTATS']._serialized_end=3844
  _globals['_CMSGCLIENTREQUESTEDCLIENTSTATS_STATSTOSEND']._serialized_start=3779
  _globals['_CMSGCLIENTREQUESTEDCLIENTSTATS_STATSTOSEND']._serialized_end=3844
  _globals['_CMSGCLIENTSTAT2']._serialized_start=3847
  _globals['_CMSGCLIENTSTAT2']._serialized_end=4039
  _globals['_CMSGCLIENTSTAT2_STATDETAIL']._serialized_start=3916
  _globals['_CMSGCLIENTSTAT2_STATDETAIL']._serialized_end=4039
  _globals['_CMSGCLIENTINVITETOGAME']._serialized_start=4041
  _globals['_CMSGCLIENTINVITETOGAME']._serialized_end=4155
  _globals['_CMSGCLIENTCHATINVITE']._serialized_start=4158
  _globals['_CMSGCLIENTCHATINVITE']._serialized_end=4343
  _globals['_CMSGCLIENTCONNECTIONSTATS']._serialized_start=4346
  _globals['_CMSGCLIENTCONNECTIONSTATS']._serialized_end=5491
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_LOGON']._serialized_start=4498
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_LOGON']._serialized_end=4837
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_UDP']._serialized_start=4839
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_UDP']._serialized_end=4952
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_VCONN']._serialized_start=4955
  _globals['_CMSGCLIENTCONNECTIONSTATS_STATS_VCONN']._serialized_end=5491
  _globals['_CMSGCLIENTSERVERSAVAILABLE']._serialized_start=5494
  _globals['_CMSGCLIENTSERVERSAVAILABLE']._serialized_end=5704
  _globals['_CMSGCLIENTSERVERSAVAILABLE_SERVER_TYPES_AVAILABLE']._serialized_start=5647
  _globals['_CMSGCLIENTSERVERSAVAILABLE_SERVER_TYPES_AVAILABLE']._serialized_end=5704
  _globals['_CMSGCLIENTREPORTOVERLAYDETOURFAILURE']._serialized_start=5706
  _globals['_CMSGCLIENTREPORTOVERLAYDETOURFAILURE']._serialized_end=5769
  _globals['_CMSGCLIENTREQUESTENCRYPTEDAPPTICKET']._serialized_start=5771
  _globals['_CMSGCLIENTREQUESTENCRYPTEDAPPTICKET']._serialized_end=5842
  _globals['_CMSGCLIENTREQUESTENCRYPTEDAPPTICKETRESPONSE']._serialized_start=5845
  _globals['_CMSGCLIENTREQUESTENCRYPTEDAPPTICKETRESPONSE']._serialized_end=5977
  _globals['_CMSGCLIENTWALLETINFOUPDATE']._serialized_start=5980
  _globals['_CMSGCLIENTWALLETINFOUPDATE']._serialized_end=6161
  _globals['_CMSGCLIENTAMGETCLANOFFICERS']._serialized_start=6163
  _globals['_CMSGCLIENTAMGETCLANOFFICERS']._serialized_end=6214
  _globals['_CMSGCLIENTAMGETCLANOFFICERSRESPONSE']._serialized_start=6216
  _globals['_CMSGCLIENTAMGETCLANOFFICERSRESPONSE']._serialized_end=6318
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORY']._serialized_start=6321
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORY']._serialized_end=6465
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORY_IDINSTANCE']._serialized_start=6436
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORY_IDINSTANCE']._serialized_end=6465
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE']._serialized_start=6468
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE']._serialized_end=6791
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE_NAMETABLEINSTANCE']._serialized_start=6595
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE_NAMETABLEINSTANCE']._serialized_end=6791
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE_NAMETABLEINSTANCE_NAMEINSTANCE']._serialized_start=6743
  _globals['_CMSGCLIENTAMGETPERSONANAMEHISTORYRESPONSE_NAMETABLEINSTANCE_NAMEINSTANCE']._serialized_end=6791
  _globals['_CMSGCLIENTDEREGISTERWITHSERVER']._serialized_start=6793
  _globals['_CMSGCLIENTDEREGISTERWITHSERVER']._serialized_end=6862
  _globals['_CMSGCLIENTCLANSTATE']._serialized_start=6865
  _globals['_CMSGCLIENTCLANSTATE']._serialized_end=7420
  _globals['_CMSGCLIENTCLANSTATE_NAMEINFO']._serialized_start=7164
  _globals['_CMSGCLIENTCLANSTATE_NAMEINFO']._serialized_end=7213
  _globals['_CMSGCLIENTCLANSTATE_USERCOUNTS']._serialized_start=7215
  _globals['_CMSGCLIENTCLANSTATE_USERCOUNTS']._serialized_end=7322
  _globals['_CMSGCLIENTCLANSTATE_EVENT']._serialized_start=7324
  _globals['_CMSGCLIENTCLANSTATE_EVENT']._serialized_end=7420
# @@protoc_insertion_point(module_scope)
