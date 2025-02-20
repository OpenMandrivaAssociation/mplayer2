%bcond_without	dlopen
%bcond_with	optimization
%bcond_with	debug

%bcond_without	yasm
%bcond_without	live
%bcond_without	theora
%bcond_with	ggi
%bcond_without	lirc
%bcond_with	xmms
%bcond_without	aa
%bcond_without	cdda
%bcond_with	compiz
%bcond_without	dirac
%bcond_without	sdl
%bcond_without	smb
%bcond_without	mga
%bcond_without	fbdev
%bcond_without	dvb
%bcond_without	fribidi
%bcond_without	enca
%bcond_without	alsa
%bcond_without	jack
%bcond_with	openal
%bcond_without	pulse
%bcond_without	schroedinger
%bcond_without	directfb
%bcond_without	v4l2
%bcond_without	vdpau
%bcond_with	ivtv

%if %{mdvver} < 201100
%bcond_with	libass
%bcond_with	vpx
%bcond_with	rtmp
%else
%bcond_without	libass
%bcond_without	vpx
%bcond_without	rtmp
%endif

%ifarch %{ix86}
%bcond_without	vesa
%endif

%if %{with dlopen}
%bcond_with	faad
%bcond_with	xvid
%bcond_with	dts
%else
%bcond_without	faad
%bcond_without	xvid
%bcond_without	dts
%endif

Name:		mplayer2
Version:	2.0
%define	gitdate	20120605
Release:	1.%{gitdate}.2
Summary:	Movie player for linux
Source0:	%{name}-%{version}-%{gitdate}.tar.xz
#gw default skin
Source4:	Blue-1.5.tar.bz2
Source5:	kernel-version.sh
Patch0:		mplayer-mdvconfig.patch
# fixes for crashes found while fixing CVE-2008-1558
Patch28:	mplayer-rtsp-extra-fixes.patch
Patch39:	mplayer2-20120605-dlopen-libfaad-libdca-and-libxvidcore.patch
Patch40:	mplayer2-20120110-fix-required-libpostproc-version.patch
URL:		https://www.mplayer2.org
License:	GPLv3
Group:		Video
BuildRequires:	ffmpeg-devel >= 0.9.1
BuildRequires:	pkgconfig(ncurses)
%if %{with aa}
BuildRequires:	aalib-devel
%endif
BuildRequires:	a52dec-devel

%if %{with jack}
BuildRequires:	pkgconfig(jack)
%endif
%if %{with pulse}
BuildRequires:	pkgconfig(libpulse)
%endif
%if %{with openal}
BuildRequires:	pkgconfig(openal)
%endif
%if %{with cdda}
BuildRequires:	cdda-devel
%endif
%if %{with dirac}
BuildRequires:	pkgconfig(dirac)  >= 0.9.0
%endif
%if %{with schroedinger}
BuildRequires:	pkgconfig(schroedinger-1.0)
%endif
BuildRequires:	libdxr3-devel
BuildRequires:	jpeg-devel
BuildRequires:	openjpeg-devel
%if %{with lirc}
BuildRequires:	pkgconfig(liblircclient0)
%endif
BuildRequires:	pkgconfig(mad)
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(libpng15)
%if %{with sdl}
BuildRequires:	pkgconfig(sdl) >= 1.1.8
%endif
%if %{with xmms}
BuildRequires:	xmms-devel
%endif
%if %{with ggi}
BuildRequires:	libggiwmh-devel
%endif
%if %{with smb}
BuildRequires:	libsmbclient-devel
%endif
%if %{with faad}
BuildRequires:	libfaad2-devel
%endif
%if %{with xvid}
BuildRequires:	xvid-devel >= 1.0.0-0.beta2.1plf
%endif
%if %{with dts}
BuildRequires:	pkgconfig(libdts)
%endif
%if %{with live}
BuildRequires:	live-devel
%endif
%if %{with vesa}
BuildRequires:	libvbe-devel liblrmi-devel
%endif
%if %{with theora}
BuildRequires:	pkgconfig(theora)
%endif
%if %{with fribidi}
BuildRequires:	pkgconfig(fribidi) >= 0.10.4
%endif
%if %{with enca}
BuildRequires:	pkgconfig(enca)
%endif
%if %{with directfb}
BuildRequires:	pkgconfig(directfb)
%endif
%if %{with vdpau}
BuildRequires:	pkgconfig(vdpau)
%endif
%if %{with libass}
BuildRequires:	pkgconfig(libass)
%endif
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(libmpg123)
%if %{with vpx}
BuildRequires:	pkgconfig(vpx)
%endif
%if %{with rtmp}
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
%if %{with yasm}
BuildRequires:	yasm
%endif
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(dvdnavmini)

%if "%{_lib}" == "lib64"
%global	_ext	()(64bit)
%else
%global	_ext	%{nil}
%endif
Suggests:	libfaad.so.2%{_ext}
Suggests:	libdca.so.0%{_ext}

#%rename		mplayer1.0
#Provides:	mplayer
#Conflicts:	mplayer-gui
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
of RealPlayer's Codecs directory in %{_libdir}/codecs/

%package	doc
Summary:	%{name} documentation
Group:		Books/Computer books
BuildArch:	noarch

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .mdv~
%patch28 -p1 -b .rtsp-extra-fixes
%patch39 -p1 -b .dlopen~
#patch40 -p1 -b .libpostproc~

echo %{gitdate} > snapshot_version

mv DOCS/README README.DOCS

%build
%if %{with optimization}
%global optflags %{nil}
%endif
%if %{with debug}
%global	optflags %{optflags} -O0
%endif
%ifarch ppc
%global	optflags %{optflags} -mcpu=7450 -maltivec
%endif
export CPPFLAGS="-I%{_includedir}/directfb"
export CFLAGS="%{optflags}"
export LDFLAGS="%{?ldflags}"
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
%if !%{with optimization}
	--enable-runtime-cpudetection \
%ifarch %{ix86}
	--enable-mmx \
	--enable-3dnow \
	--enable-sse \
	--enable-sse2 \
	--enable-fastmemcpy \
%endif
%endif
%if !%{with dts}
	--disable-libdca \
	--enable-libdca-dlopen \
%endif
	--enable-nas \
%if %{with debug}
	--enable-debug=3 \
%else
	--disable-sighandler \
%endif
	--language=all \
%if ! %{with faad}
	--disable-faad \
	--enable-faad-dlopen \
%endif
%if ! %{with xvid}
	--disable-xvid \
	--enable-xvid-dlopen \
%endif
	--disable-libdvdcss-internal \
%if %{with lirc}
	--enable-lirc \
%else
	--disable-lirc \
%endif
	--enable-tv \
%if ! %{with v4l2}
	--disable-tv-v4l2 \
%endif
	--enable-joystick \
	--enable-gl \
	--disable-svga \
%if ! %{with mga}
	--disable-mga \
%endif
%if ! %{with fbdev}
	--disable-fbdev \
%endif
%if %{with directfb}
	--enable-directfb \
%else
	--disable-directfb \
%endif
%if ! %{with live}
	--disable-live \
%endif
%if ! %{with vesa}
	--disable-vesa \
%endif
%if %{!with theora}
	--disable-theora \
%endif
%if %{with xmms}
	--enable-xmms \
	--with-xmmslibdir=%{_libdir} \
%endif
%if %{with smb}
	--enable-smb \
%endif
%if ! %{with dvb}
	--disable-dvb \
	--disable-dvbhead \
%endif
%if ! %{with ggi}
	--disable-ggi \
%endif
	--codecsdir=%{_libdir}/codecs \
%if ! %{with jack}
	--disable-jack \
%endif
%if ! %{with aa}
	--disable-aa \
%endif
%if ! %{with cdda}
	--disable-cdparanoia \
%endif
%if ! %{with sdl}
	--disable-sdl \
%endif
%if ! %{with alsa}
	--disable-alsa \
%endif
%if ! %{with fribidi}
	--disable-fribidi \
%endif
%if !%{with enca}
	--disable-enca \
%endif
%if %{with pulse}
	--enable-pulse \
%else
	--disable-pulse \
%endif
%if !%{with openal}
	--disable-openal \
%endif
%if ! %{with ivtv}
	--disable-ivtv \
%endif
%if ! %{with vdpau}
	--disable-vdpau \
%endif
	--enable-dvdnav \
	--disable-dvdread-internal \
	--enable-dvdread

%make

%install
install -m755 mplayer -D %{buildroot}%{_bindir}/mplayer2
install -m644 etc/example.conf -D %{buildroot}%{_sysconfdir}/mplayer2/mplayer2.conf

for lang in de fr hu pl es it zh_CN en; do
	install -m644 DOCS/man/$lang/mplayer.1 -D %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mplayer2.1
done 
%find_lang mplayer2 --with-man

%files -f mplayer2.lang
%doc AUTHORS README Copyright
%dir %{_sysconfdir}/mplayer2
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer2/mplayer2.conf
%{_bindir}/mplayer2
%{_mandir}/man1/mplayer2.1*

%files doc
%doc README.DOCS
%doc DOCS/default.css DOCS/xml DOCS/tech/
