Summary:	On-screen keyboard
Name:		caribou
Version:	0.4.13
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/caribou/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	e4913478c220f7df6fd5adef6f654c0e
URL:		http://live.gnome.org/Caribou
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libxklavier-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	python-pygobject3-devel
BuildRequires:	vala-vapigen
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	glib-gio-gsettings
Requires:	python-pyatspi
Requires:	python-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/caribou

%description
Caribou is an on-screen keyboard suitable for people who can use a
mouse but not a hardware keyboard. This on-screen keyboard may also be
useful for touch screen or tablet users.

%package libs
Summary:	Caribou library
Group:		Libraries

%description libs
Caribou library.

%package devel
Summary:	Development files for Caribou
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package provides development files for Caribou.

%package gtk+-module
Summary:	GTK+ IM module for %{name}
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description gtk+-module
This package contains caribou IM module for GTK+.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libcaribou-gtk-module.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/caribou
%attr(755,root,root) %{_bindir}/caribou-preferences

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/antler-keyboard

%{_datadir}/antler
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml

%{_datadir}/caribou
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop
%{py_sitescriptdir}/caribou

%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcaribou.so.?
%attr(755,root,root) %{_libdir}/libcaribou.so.*.*.*
%{_libdir}/girepository-1.0/Caribou-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaribou.so
%{_includedir}/libcaribou
%{_datadir}/gir-1.0/Caribou-1.0.gir
%{_pkgconfigdir}/*.pc
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files gtk+-module
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so

