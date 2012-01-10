%define build_plf 0
%define build_optimization 0
%define build_debug 0

%define build_yasm	1
%define build_live	1
%define build_vesa	1
%define build_theora	1
%define build_ggi	0
%define build_lirc	1
%define	build_xmms	0
%define	build_arts	0
%define build_aa	1
%define build_cdda	1
%define build_compiz	0
%define build_dirac	1
%define build_sdl	1
%define build_smb	1
%define build_mga	1
%define build_fbdev	1
%define build_dvb	1
%define build_fribidi	1
%define build_enca	1
%define build_alsa	1
%define build_jack	1
%define build_openal	0
%define build_pulse	1
%define build_schroedinger	1
%define build_faac 0
%define build_faad 0
%define build_x264 0
%define build_xvid 0
%define build_dts 0
%define build_directfb 1
%define build_v4l2 1
%define build_vdpau 1
%define build_ivtv 0
%define build_libass 1
%define build_vpx 1
%define build_rtmp 1

%if %mdvver < 201100 && !%build_plf
%define build_libass 0
%define build_vpx 0
%define build_rtmp 0
%endif

%ifnarch %{ix86}
%define build_vesa 0
%endif

%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define build_faac 1
%define build_faad 1
%define build_x264 1
%define build_xvid 1
%define build_dts 1
%define build_yasm 1
%define build_dirac 1
%define build_schroedinger 1
%endif

%{?_with_live: %{expand: %%global build_live 1}}
%{?_without_live: %{expand: %%global build_live 0}}
%{?_with_yasm: %{expand: %%global build_yasm 1}}
%{?_without_yasm: %{expand: %%global build_yasm 0}}
%{?_with_vesa: %{expand: %%global build_vesa 1}}
%{?_without_vesa: %{expand: %%global build_vesa 0}}
%{?_with_optimization: %{expand: %%global build_optimization 1}}
%{?_with_debug: %{expand: %%global build_debug 1}}
%{?_without_debug: %{expand: %%global build_debug 0}}
%{?_with_theora: %{expand: %%global build_theora 1}}
%{?_without_theora: %{expand: %%global build_theora 0}}
%{?_with_smb: %{expand: %%global build_smb 1}}
%{?_without_smb: %{expand: %%global build_smb 0}}
%{?_with_ggi: %{expand: %%global build_ggi 1}}
%{?_without_ggi: %{expand: %%global build_ggi 0}}
%{?_with_lirc: %{expand: %%global build_lirc 1}}
%{?_without_lirc: %{expand: %%global build_lirc 0}}
%{?_with_xmms: %{expand: %%global build_xmms 1}}
%{?_without_xmms: %{expand: %%global build_xmms 0}}
%{?_with_arts: %{expand: %%global build_arts 1}}
%{?_without_arts: %{expand: %%global build_arts 0}}
%{?_with_aa: %{expand: %%global build_aa 1}}
%{?_without_aa: %{expand: %%global build_aa 0}}
%{?_with_cdda: %{expand: %%global build_cdda 1}}
%{?_without_cdda: %{expand: %%global build_cdda 0}}
%{?_with_dirac: %{expand: %%global build_dirac 1}}
%{?_without_dirac: %{expand: %%global build_dirac 0}}
%{?_with_sdl: %{expand: %%global build_sdl 1}}
%{?_without_sdl: %{expand: %%global build_sdl 0}}
%{?_with_mga: %{expand: %%global build_mga 1}}
%{?_without_mga: %{expand: %%global build_mga 0}}
%{?_with_fribidi: %{expand: %%global build_fribidi 1}}
%{?_without_fribidi: %{expand: %%global build_fribidi 0}}
%{?_with_enca: %{expand: %%global build_enca 1}}
%{?_without_enca: %{expand: %%global build_enca 0}}
%{?_with_jack: %{expand: %%global build_jack 1}}
%{?_without_jack: %{expand: %%global build_jack 0}}
%{?_with_libass: %{expand: %%global build_libass 1}}
%{?_without_libass: %{expand: %%global build_libass 0}}
%{?_with_pulse: %{expand: %%global build_pulse 1}}
%{?_without_pulse: %{expand: %%global build_pulse 0}}
%{?_with_openal: %{expand: %%global build_openal 1}}
%{?_without_openal: %{expand: %%global build_openal 0}}
%{?_with_schroedinger: %{expand: %%global build_schroedinger 1}}
%{?_without_schroedinger: %{expand: %%global build_schroedinger 0}}
%{?_with_faac: %{expand: %%global build_faac 1}}
%{?_without_faac: %{expand: %%global build_faac 0}}
%{?_with_faad: %{expand: %%global build_faad 1}}
%{?_without_faad: %{expand: %%global build_faad 0}}
%{?_with_x264: %{expand: %%global build_x264 1}}
%{?_without_x264: %{expand: %%global build_x264 0}}
%{?_with_xvid: %{expand: %%global build_xvid 1}}
%{?_without_xvid: %{expand: %%global build_xvid 0}}
%{?_with_dts: %{expand: %%global build_dts 1}}
%{?_without_dts: %{expand: %%global build_dts 0}}
%{?_with_directfb: %{expand: %%global build_directfb 1}}
%{?_without_directfb: %{expand: %%global build_directfb 0}}
%{?_with_rtmp: %{expand: %%global build_rtmp 1}}
%{?_without_rtmp: %{expand: %%global build_rtmp 0}}
%{?_with_v4l2: %{expand: %%global build_v4l2 1}}
%{?_without_v4l2: %{expand: %%global build_v4l2 0}}
%{?_with_vdpau: %{expand: %%global build_vdpau 1}}
%{?_without_vdpau: %{expand: %%global build_vdpau 0}}
%{?_with_vpx: %{expand: %%global build_vpx 1}}
%{?_without_vpx: %{expand: %%global build_vpx 0}}

Name:		mplayer2
Version:	2.0
%define	gitdate	20120110
Release:	1.%{gitdate}.1%{?extrarelsuffix}
Summary:	Movie player for linux
Source0:	%{name}-%{version}-%{gitdate}.tar.xz
#gw default skin
Source4:	Blue-1.5.tar.bz2
Source5:	kernel-version.sh
Patch0:		mplayer-mdvconfig.patch
# fixes for crashes found while fixing CVE-2008-1558
Patch28:	mplayer-rtsp-extra-fixes.patch
Patch39:	mplayer-dlopen-libfaac-libfaad-and-libx264.patch
Patch40:	mplayer2-20120110-fix-required-libpostproc-version.patch
URL:		http://www.mplayerhq.hu
License:	GPLv3
Group:		Video
BuildRequires:	ffmpeg-devel >= 0.9.1
BuildRequires:	pkgconfig(ncurses)
%if %build_aa
BuildRequires:	aalib-devel
%endif
BuildRequires:  a52dec-devel
%if %build_arts
BuildRequires:  arts-devel
%endif

%if %build_jack
BuildRequires:  pkgconfig(jack)
%endif
%if %build_pulse
BuildRequires:  pkgconfig(libpulse)
%endif
%if %build_openal
BuildRequires:  pkgconfig(openal)
%endif
%if %build_cdda
BuildRequires:	cdda-devel
%endif
%if %build_dirac
BuildRequires:	pkgconfig(dirac)  >= 0.9.0
%endif
%if %build_schroedinger
BuildRequires:	pkgconfig(schroedinger-1.0)
%endif
BuildRequires:	libdxr3-devel
BuildRequires:	jpeg-devel
BuildRequires:	openjpeg-devel
%if %build_lirc
BuildRequires:	pkgconfig(liblircclient0)
%endif
BuildRequires:  pkgconfig(mad)
BuildRequires:  nas-devel
BuildRequires:	pkgconfig(libpng15)
%if %build_sdl
BuildRequires:	pkgconfig(sdl) >= 1.1.8
%endif
%if %build_xmms
BuildRequires:  xmms-devel
%endif
%if %build_ggi
BuildRequires:	libggiwmh-devel
%endif
%if %build_smb
BuildRequires:	libsmbclient-devel
%endif
%if %build_faac
BuildRequires:	libfaac-devel
%endif
%if %build_faad
BuildRequires:	libfaad2-devel
%endif
%if %build_x264
BuildRequires:	pkgconfig(x264) >= 0.120
%endif
%if %build_xvid
BuildRequires:	xvid-devel >= 1.0.0-0.beta2.1plf
%endif
%if %build_dts
BuildRequires:	pkgconfig(libdts)
%endif
%if %build_live
BuildRequires:	live-devel
%endif
%if %build_vesa
BuildRequires:	libvbe-devel liblrmi-devel
%endif
%if %build_theora
BuildRequires:	pkgconfig(theora)
%endif
%if %build_fribidi
BuildRequires:	pkgconfig(fribidi) >= 0.10.4
%endif
%if %build_enca
BuildRequires:	pkgconfig(enca)
%endif
%if %build_directfb
BuildRequires:	pkgconfig(directfb)
%endif
%if %build_vdpau
BuildRequires:	pkgconfig(vdpau)
%endif
%if %build_libass
BuildRequires:	pkgconfig(libass)
%endif
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(libmpg123)
%if %build_vpx
BuildRequires:	pkgconfig(vpx)
%endif
%if %build_rtmp
BuildRequires:	pkgconfig(librtmp)
%endif
BuildRequires:	bzip2-devel
BuildRequires:	mng-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(speex)
BuildRequires:	libmpcdec-devel
BuildRequires:	ladspa-devel
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(caca)
%if %mdvver >= 201010
BuildRequires:	giflib-devel
%else
BuildRequires:	ungif-devel
%endif
%if %build_yasm
BuildRequires:	yasm
%endif
BuildRequires:	pkgconfig(libbs2b)
%if "%{_lib}" == "lib64"
%global	_ext	()(64bit)
%else
%global	_ext	%{nil}
%endif
Suggests:	libfaac.so.0%{_ext}
Suggests:	libfaad.so.2%{_ext}
Suggests:	libx264.so.120%{_ext}
Suggests:	libdca.so.0%{_ext}
Suggests:	libdvdcss.so.2%{_ext}

%rename		mplayer1.0
%rename		mplayer
Conflicts:	mplayer-gui
# we might wanna allow for mencoder to still be packaged..
#Conflicts:	mencoder


%description
MPlayer is a movie player for LINUX (runs on many other Unices, and
non-x86 CPUs, see the documentation). It plays most MPEG, VOB, AVI,
VIVO, ASF/WMV, QT/MOV, FLI, NuppelVideo, yuv4mpeg, FILM, RoQ, and some
RealMedia files, supported by many native, XAnim, and Win32 DLL codecs.
You can watch VideoCD, SVCD, DVD, 3ivx, FLI, and even DivX movies too
(and you don't need the avifile library at all!). The another big
feature of mplayer is the wide range of supported output drivers. It
works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, but you can use
SDL (and this way all drivers of SDL), VESA (on every VESA compatible
card, even without X!), and some lowlevel card-specific drivers (for
Matrox, 3Dfx and Radeon) too! Most of them supports software or hardware
scaling, so you can enjoy movies in fullscreen. MPlayer supports
displaying through some hardware MPEG decoder boards, such as the DVB
and DXR3/Hollywood+! And what about the nice big antialiased shaded
subtitles (9 supported types!!!) with european/ISO 8859-1,2 (hungarian,
english, czech, etc), cyrillic, korean fonts, and OSD?

Note: If you want to play Real content, you need to have the content
of RealPlayer's Codecs directory in %_libdir/codecs/
%if %build_plf

This package is in PLF because some included codecs are covered by
patents.  It also includes support for reading DVDs encrypted with CSS
which might be illegal in some countries.

For non-free binary codecs support you should install the packages
win32-codecs, real-codecs and xanim-codecs.
%endif

%package	doc
Summary:	%{name} documentation
Group:		Books/Computer books

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .mdv~
%patch28 -p1 -b .rtsp-extra-fixes
#patch39 -p1 -b .dlopen~
%patch40 -p1 -b .libpostproc~

perl -pi -e 's^r\$git_revision^%{gitdate}^' version.sh

mv DOCS/README README.DOCS

%build
%if !%build_optimization
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
%endif
%if %build_debug
export CFLAGS="$CFLAGS -g"
%endif
%ifarch ppc
export CFLAGS="$CFLAGS -mcpu=7450 -maltivec"
%endif
%if %build_directfb
export CPPFLAGS="-I%{_includedir}/directfb"
%endif
export LDFLAGS="%{?ldflags}"
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}/%{name} \
	--confdir=%{_sysconfdir}/%{name} \
	--libdir=%{_libdir} \
%if !%build_optimization
	--enable-runtime-cpudetection \
%if !%build_dts
	--disable-libdca \
%if 0
	--enable-libdca-dlopen \
%endif
%endif
%ifarch %{ix86}
        --enable-mmx \
        --enable-3dnow \
        --enable-sse \
        --enable-sse2 \
        --enable-fastmemcpy \
%endif
%endif
	--enable-freetype \
	--enable-nas \
%if %build_debug
	--enable-debug=3 \
%else
	--disable-sighandler \
%endif
	--language=all \
	\
%if ! %build_faad
	--disable-faad \
%if 0
	--enable-faad-dlopen \
%endif
%endif
%if 0
#!%build_faac
	--enable-faac-dlopen \
%endif
%if 0
#!%build_x264
	--enable-x264-dlopen \
%endif
	--disable-libdvdcss-internal \
%if %build_lirc
	--enable-lirc \
%else
	--disable-lirc \
%endif
	--enable-tv \
%if ! %build_v4l2
	--disable-tv-v4l2 \
%endif
	--enable-joystick \
	\
	--enable-gl \
        --disable-svga \
%if ! %build_mga
	--disable-mga \
%endif
%if ! %build_fbdev
	--disable-fbdev \
%endif
%if %build_directfb
       --enable-directfb \
%else
       --disable-directfb \
%endif
%if ! %build_live
	--disable-live \
%endif
%if ! %build_vesa
       --disable-vesa \
%endif
%if %build_theora
	--enable-theora \
%else
	--disable-theora \
%endif
%if %build_xmms
	--enable-xmms --with-xmmslibdir=%{_libdir} \
%endif
%if %build_smb
	--enable-smb \
%endif
%if ! %build_dvb
       --disable-dvb \
       --disable-dvbhead \
%endif
%if ! %build_ggi
	--disable-ggi \
%endif
	--codecsdir=%{_libdir}/codecs \
%if ! %build_arts
	--disable-arts \
%endif
%if ! %build_jack
	--disable-jack \
%endif
%if ! %build_aa
	--disable-aa \
%endif
%if ! %build_cdda
	--disable-cdparanoia \
%endif
%if ! %build_sdl
	--disable-sdl \
%endif
%if ! %build_alsa
	--disable-alsa \
%endif
%if ! %build_fribidi
	--disable-fribidi \
%endif
%if !%build_enca
	--disable-enca \
%endif
%if %build_pulse
	--enable-pulse \
%endif
%if !%build_openal
	--disable-openal \
%endif
%if ! %build_ivtv
	--disable-ivtv \
%endif
%if ! %build_vdpau
	--disable-vdpau \
%endif


# Keep this line before empty end %%configure (ppc conditionnal pb)
make EXESUF=%{pkgext}
#gw make sure we have our version string included:
fgrep %{release} version.h

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m755 mplayer%{pkgext} -D %{buildroot}%{_bindir}/mplayer%{pkgext}
for lang in de fr hu pl es it zh_CN en; do
    install -m644 DOCS/man/$lang/mplayer.1 -D %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mplayer%{pkgext}.1
done 
%find_lang mplayer%{pkgext} --with-man

install -m 644 etc/example.conf %{buildroot}%{_sysconfdir}/%{name}/mplayer.conf

%if %build_debug
export DONT_STRIP=1
%endif

%files -f mplayer%{pkgext}.lang
%doc AUTHORS README Copyright
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/mplayer.conf
%{_bindir}/mplayer%{pkgext}
%{_mandir}/man1/mplayer%{pkgext}.1*
%dir %{_datadir}/%{name}

%files doc
%doc README.DOCS
%doc DOCS/default.css DOCS/xml DOCS/tech/
