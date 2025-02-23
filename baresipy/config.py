DEFAULT = """#
# baresip configuration
#

#------------------------------------------------------------------------------

# Core
poll_method		epoll		# poll, select, epoll ..

# SIP
sip_trans_bsize		128
#sip_listen		0.0.0.0:5060
#sip_certificate	cert.pem

# Call
call_local_timeout	120
call_max_calls		4

# Audio
#audio_path		/usr/share/baresip
audio_player		alsa,default
audio_source		alsa,default
audio_alert		alsa,default
ausrc_srate		48000
#auplay_srate		48000
ausrc_channels		2
#auplay_channels	0
#audio_txmode		poll		# poll, thread
audio_level		no
ausrc_format		s16		# s16, float, ..
auplay_format		s16		# s16, float, ..
auenc_format		s16		# s16, float, ..
audec_format		s16		# s16, float, ..

# Video
#video_source		v4l2,/dev/video0
#video_display		x11,nil
video_size		352x288
video_bitrate		500000
video_fps		25.00
video_fullscreen	yes
videnc_format		yuv420p

# AVT - Audio/Video Transport
rtp_tos			184
#rtp_ports		10000-20000
#rtp_bandwidth		512-1024 # [kbit/s]
rtcp_mux		no
jitter_buffer_delay	5-10		# frames
rtp_stats		no
#rtp_timeout		60

# Network
#dns_server		10.0.0.1:53
#net_interface		wlp0s20f3

# BFCP
#bfcp_proto		udp

#------------------------------------------------------------------------------
# Modules

module_path		/usr/lib/baresip/modules

# UI Modules
module			stdio.so
#module			cons.so
#module			evdev.so
#module			httpd.so

# Audio codec Modules (in order)
module			opus.so
#module			amr.so
#module			g7221.so
#module			g722.so
#module			g726.so
module			g711.so
#module			gsm.so
#module			l16.so
#module			bv32.so
#module			mpa.so
#module			codec2.so
#module			ilbc.so
#module			isac.so

# Audio filter Modules (in encoding order)
module			vumeter.so
#module			sndfile.so
#module			speex_aec.so
#module			speex_pp.so
#module			plc.so

# Audio driver Modules
module			alsa.so
module			pulse.so
#module			jack.so
#module			portaudio.so
#module			aubridge.so
module			aufile.so

# Video codec Modules (in order)
module			avcodec.so
#module			vp8.so
#module			vp9.so
#module			h265.so

# Video filter Modules (in encoding order)
#module			selfview.so
#module			snapshot.so
#module			swscale.so
#module			vidinfo.so

# Video source modules
#module			v4l.so
#module			v4l2.so
#module			v4l2_codec.so
#module			avformat.so
#module			x11grab.so
#module			cairo.so
#module			vidbridge.so

# Video display modules
#module			directfb.so
#module			x11.so
#module			sdl2.so
#module			fakevideo.so

# Audio/Video source modules
#module			rst.so
#module			gst1.so
#module			gst_video1.so

# Media NAT modules
module			stun.so
module			turn.so
module			ice.so
#module			natpmp.so
#module			pcp.so

# Media encryption modules
#module			srtp.so
#module			dtls_srtp.so
#module			zrtp.so


#------------------------------------------------------------------------------
# Temporary Modules (loaded then unloaded)

module_tmp		uuid.so
module_tmp		account.so


#------------------------------------------------------------------------------
# Application Modules

module_app		auloop.so
#module_app		b2bua.so
module_app		contact.so
module_app		debug_cmd.so
#module_app		dtmfio.so
#module_app		echo.so
#module_app		gtk.so
module_app		menu.so
#module_app		mwi.so
#module_app		natbd.so
#module_app		presence.so
#module_app		syslog.so
#module_app		mqtt.so
#module_app		ctrl_tcp.so
module_app		vidloop.so


#------------------------------------------------------------------------------
# Module parameters


cons_listen		0.0.0.0:5555

http_listen		0.0.0.0:8000

ctrl_tcp_listen		0.0.0.0:4444

evdev_device		/dev/input/event0

# Opus codec parameters
opus_bitrate		28000 # 6000-510000
#opus_stereo		yes
#opus_sprop_stereo	yes
#opus_cbr		no
#opus_inband_fec	no
#opus_dtx		no
#opus_mirror		no
#opus_complexity		10
#opus_application		audio	# {voip,audio}

vumeter_stderr		yes

# Selfview
video_selfview		window # {window,pip}
#selfview_size		64x64

# ICE
ice_turn		no
ice_debug		no
ice_nomination		regular	# {regular,aggressive}
ice_mode		full	# {full,lite}

# ZRTP
#zrtp_hash		no  # Disable SDP zrtp-hash (not recommended)

# Menu
#menu_bell		yes
#redial_attempts	3 # Num or <inf>
#redial_delay		5 # Delay in seconds
#ringback_disabled	yes
#statmode_default	off"""
