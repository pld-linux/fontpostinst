Summary:	Font post (un)installation script
Summary(pl):	Skrypt po(de)instalacyjny dla fontów
Name:		fontpostinst
Version:	0.1
Release:	3
License:	Free
Group:		Applications/System
Source0:	%{name}
Requires:	fileutils
Requires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script to be called after each fonts installation or uninstallation.
It supports regeneration of XFree86 fonts.alias, fonts.scale,
fonts.dir files, gnome-font catalogs, ghostscript Fontmaps and
fontconfig/xft cache.

%description -l pl
Skrypt do wywo³ywania po ka¿dym instalowaniu lub odinstalowaniu
fontów. Potrafi regenerowaæ pliki fonts.alias, fonts.scale i fonts.dir
XFree86, katalogi gnome-font, pliki Fontmap ghostscripta oraz cache
fontconfig/xft.

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
