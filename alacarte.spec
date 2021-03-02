Summary:	Menu editor for the GNOME desktop
Summary(pl.UTF-8):	Edytor menu dla GNOME
Name:		alacarte
Version:	3.36.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/alacarte/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	f890c79646c3ecfed4883d56442d1142
URL:		https://gitlab.gnome.org/GNOME/alacarte
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools
BuildRequires:	gnome-menus-devel >= 3.5.3
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme >= 0.10-3
Requires:	gnome-menus >= 3.5.3
Requires:	gtk+3 >= 3.0
Requires:	python-pygobject3 >= 3.0
# for help
Suggests:	gnome-user-docs >= 3.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alacarte is a simple freedesktop.org compliant menu editor for GNOME
that lets you change your menus, simply and quickly.

%description -l pl.UTF-8
Alacarte jest prostym, zgodnym z freedesktop.org edytorem menu dla
GNOME pozwalającym w szybki i łatwy sposób dostosować menu do własnych
potrzeb.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/io

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/alacarte
%{py3_sitescriptdir}/Alacarte
%{_datadir}/alacarte
%{_desktopdir}/alacarte.desktop
%{_iconsdir}/hicolor/*x*/apps/alacarte.png
%{_mandir}/man1/alacarte.1*
