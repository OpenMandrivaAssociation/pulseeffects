Name:           pulseeffects
Version:        4.8.4
Release:        1
Summary:        Audio equalizer, filters and effects for Pulseaudio applications
License:        GPLv3
Group:          Sound/Mixers
Url:            https://github.com/wwmm/pulseeffects
Source0:        https://github.com/wwmm/pulseeffects/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  appstream-util
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  libxml2-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(rnnoise)

Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-plugins-good
Requires:       swh-plugins
Requires:       lsp-plugins
Requires:       %{_lib}rnnoise0
# Recommends because is optional and in contrib/unsupported repo
Recommends:     lv2-calf-plugins
Recommends:     rubberband
# Not packaged yet
Recommends:     mda-lv2
Recommends:     ladspa-zam-plugins
Recommends:     lv2-zam-plugins
Recommends:     zam-plugins

# Need for RNNoise
#Recommends: RNNoise

%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PulseAudio applications.

%prep
%autosetup -p1
rm -rf build && mkdir build

%build
export LC_ALL="${LC_ALL:-UTF-8}"
cd build
meson --prefix=/usr ..
%ninja_build
cd ..

%install
export LC_ALL="${LC_ALL:-UTF-8}"
cd build
%ninja_install
cd ..

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
    --add-category='X-Mageia-CrossDesktop' \
    --dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE.md README.md
%{_bindir}/pulseeffects
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/*
%{_datadir}/metainfo/com.github.wwmm.pulseeffects.appdata.xml
%{_datadir}/help/*/%{name}/
%{_datadir}/dbus-1/services/com.github.wwmm.pulseeffects.service
%{_libdir}/gstreamer-1.0/libgst*.so
