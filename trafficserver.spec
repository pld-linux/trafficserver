Summary:	Fast, scalable and extensible HTTP/1.1 compliant caching proxy server
Name:		trafficserver
Version:	2.0.0
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/HTTP
Source0:	http://www.apache.org/dist/trafficserver/%{name}-%{version}.tar.bz2
# Source0-md5:	4c000131b19bdda05f1f21c6ae0547af
URL:		http://trafficserver.apache.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
