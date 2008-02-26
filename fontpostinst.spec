Summary:	Font post (un)installation script
Summary(pl.UTF-8):	Skrypt po(de)instalacyjny dla fontów
Name:		fontpostinst
Version:	0.1
Release:	15
License:	Free
Group:		Applications/System
Source0:	%{name}
Requires:	fileutils
Requires:	textutils
Suggests:	fontconfig
Suggests:	t1lib
Suggests:	xorg-app-mkfontdir
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script to be called after each fonts installation or uninstallation.
It supports regeneration of XFree86 fonts.alias, fonts.scale,
fonts.dir files, gnome-font catalogs, ghostscript Fontmaps,
fontconfig/xft cache and t1lib FontDatabase.

%description -l pl.UTF-8
Skrypt do wywoływania po każdym instalowaniu lub odinstalowaniu
fontów. Potrafi regenerować pliki fonts.alias, fonts.scale i fonts.dir
XFree86, katalogi gnome-font, pliki Fontmap ghostscripta, cache
fontconfig/xft oraz plik FontDatabase t1lib.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
