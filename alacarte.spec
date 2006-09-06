Summary:	Menu editor for the GNOME desktop
Summary(pl):	Edytor menu dla GNOME
Name:		alacarte
Version:	0.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/alacarte/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	646c9d5619d25e8d7676289d892bb761
URL:		http://www.realistanew.com/projects/alacarte/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-menus-devel >= 2.16.0
BuildRequires:	intltool >= 0.35
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python-pygtk-devel >= 2:2.9.6
Requires(post,postun):	gtk+2 >= 2:2.10.2
Requires(post,postun):	hicolor-icon-theme
%pyrequires_eq	python-modules
Requires:	python-pygtk-glade >= 2:2.9.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alacarte is a simple freedesktop.org compliant menu editor for GNOME
that lets you change your menus, simply and quickly.

%description -l pl
Alacarte jest prostym, zgodnym z freedesktop.org edytorem menu dla
GNOME pozwalaj±cym w szybki i ³atwy sposób dostosowaæ menu do w³asnych
potrzeb.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	PYTHON="/usr/bin/python"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/Alacarte/*.py

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/Alacarte
%{py_sitedir}/Alacarte/*.py[co]
%{_datadir}/%{name}
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*/*
