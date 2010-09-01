Summary:	Fast, scalable and extensible HTTP/1.1 compliant caching proxy server
Name:		trafficserver
Version:	2.0.1
Release:	1
License:	Apache v2.0
Group:		Networking/Daemons/HTTP
Source0:	http://www.apache.org/dist/trafficserver/%{name}-%{version}.tar.bz2
# Source0-md5:	94fc8b032eea873a1a4838249c0408a2
URL:		http://trafficserver.apache.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

%description
Traffic Server is fast, scalable and extensible HTTP/1.1 compliant
caching proxy server. Formerly a commercial product, Yahoo! donated it
to the Apache Foundation, and is now an Apache TLP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL NOTICE README STATUS
