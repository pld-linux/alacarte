Summary:	Menu editor for the GNOME desktop
Summary(pl.UTF-8):	Edytor menu dla GNOME
Name:		alacarte
Version:	0.13.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/alacarte/0.13/%{name}-%{version}.tar.bz2
# Source0-md5:	b45232eaf093e7e1fbf99b335d8b880c
URL:		http://www.realistanew.com/projects/alacarte/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-menus-devel >= 2.28.0
BuildRequires:	intltool >= 0.37.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme >= 0.10-3
Requires:	gnome-menus-editor >= 2.28.0
Requires:	python-gnome-ui
Requires:	python-pygobject >= 2.16.0
Requires:	python-pygtk-glade >= 2:2.12.0
# for help
Suggests:	gnome-user-docs >= 2.24.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%{__automake}
%{__autoconf}
%configure \
	PYTHON="/usr/bin/python"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# not supported by glibc
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{bem,en@shaw,io}

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
%dir %{py_sitescriptdir}/Alacarte
%{py_sitescriptdir}/Alacarte/*.py[co]
%{_datadir}/alacarte
%{_desktopdir}/alacarte.desktop
%{_iconsdir}/hicolor/*/*/*
