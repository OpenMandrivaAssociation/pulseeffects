Name:           pulseeffects
Version:        4.4.6
Release:        2
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

#Need import.
Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-plugins-good
#Requires:       ladspa-plugins-swh
Requires:       lv2-calf-plugins

%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PulseAudio applications.

%prep
%autosetup -p1
rm -rf build && mkdir build

%build
export LC_ALL="${LC_ALL:-UTF-8}"
pushd build
meson --prefix=/usr ..
%ninja_build
popd

%install
export LC_ALL="${LC_ALL:-UTF-8}"
pushd build
%ninja_install
popd

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
%{_datadir}/help/C/%{name}/*
%{_datadir}/help/pt_BR/%{name}/*
%{_datadir}/help/ru/%{name}/*
%{_datadir}/dbus-1/services/com.github.wwmm.pulseeffects.service
%{_libdir}/gstreamer-1.0/libgst*.so
