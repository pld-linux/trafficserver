# TODO:
# - create devel, perl-Apache-TS packages
# - add init/systemctl scripts
# - fix file attrs
# - fix perl paths
#
Summary:	Fast, scalable and extensible HTTP/1.1 compliant caching proxy server
Name:		trafficserver
Version:	4.2.0
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/HTTP
Source0:	http://www.apache.org/dist/trafficserver/%{name}-%{version}.tar.bz2
# Source0-md5:	a4302d1650eac9bc7d4cab27985668d1
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
%define		skip_post_check_so	.*lib.*/libtsmgmtshare.so.*

%include	/usr/lib/rpm/macros.perl

%description
Traffic Server is fast, scalable and extensible HTTP/1.1 compliant
caching proxy server. Formerly a commercial product, Yahoo! donated it
to the Apache Foundation, and is now an Apache TLP.

%prep
%setup -q

%build
%configure \
--sysconfdir=%{_sysconfdir}/trafficserver
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT/usr/man/man3/Apache* $RPM_BUILD_ROOT%{_mandir}/man3/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL NOTICE README STATUS
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/body_factory
%dir %{_sysconfdir}/%{name}/body_factory/default
%{_sysconfdir}/%{name}/body_factory/default/.body_factory_info
%{_sysconfdir}/%{name}/body_factory/default/*
%{_sysconfdir}/%{name}/*.config
%{_sysconfdir}/%{name}/stats.config.xml
%{_sysconfdir}/%{name}/trafficserver-release
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.so.*
%{_docdir}/trafficserver/trafficshell/*.1
%{_mandir}/man1/*
%{_mandir}/man3/TS*
%{_mandir}/man5/*
%{_mandir}/man8/*

#%files devel
#%defattr(644,root,root,755)
%{_includedir}/ts/*.h
%{_libdir}/*.la
%{_libdir}/*.so

#%files -n perl-Apache-TS
#%defattr(644,root,root,755)
%{_datadir}/perl5/Apache/TS.pm
%{_datadir}/perl5/Apache/TS.pm.in
%{_datadir}/perl5/Apache/TS/AdminClient.pm
%{_datadir}/perl5/Apache/TS/Config.pm
%{_datadir}/perl5/Apache/TS/Config/Records.pm
%{_prefix}/lib/perl5/5.18.0/x86_64-pld-linux-thread-multi/auto/Apache/TS/.packlist
%{_libdir}/perl5/5.18.2/x86_64-pld-linux-thread-multi/perllocal.pod
%{_mandir}/man3/Apache*

