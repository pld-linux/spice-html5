# TODO: apache config / webappize? (probably doesn't even need any web server though)
Summary:	Pure JavaScript SPICE client
Summary(pl.UTF-8):	Klient SPICE w czystym JavaScripcie
Name:		spice-html5
Version:	0.1.1
Release:	1
License:	LGPL v3+
Group:		Applications/Networking
Source0:	http://spice-space.org/download/spice-html5/%{name}-%{version}.tar.gz
# Source0-md5:	9f0a2a48b372b42eefa6ae654bc5afcf
URL:		http://spice-space.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spice-html5 is a JavaScript SPICE client. This includes a simple HTML
page to initiate a session, and the client itself. It includes a
configuration file for Apache, but should work with any web server.

%description -l pl.UTF-8
spice-html5 to klient SPICE napisany w JavaScripcie. Zawiera prostą
stronę HTML do rozpoczynania sesji oraz właściwego klienta. Dołączony
jest plik konfiguracyjny dla Apache'a, ale powinien działać z dowolnym
serwerem WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_datadir}/spice-html5
#/etc/httpd/conf.d/spice-html5.conf
