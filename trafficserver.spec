# TODO:
# - create devel, perl-Apache-TS packages
# - add init/systemctl scripts
# - fix file attrs
# - fix perl paths
# - move perl files to perl vendordir
# - non lib-prefixed *.so should go to private lib dir?, do we need .la?
# - %config attrs to sysconfig files

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
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sqlite3-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed
%define		skip_post_check_so	.*lib.*/libtsmgmtshare.so.*

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

%{__mv} $RPM_BUILD_ROOT/usr/man/man3/Apache* $RPM_BUILD_ROOT%{_mandir}/man3
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/perl5/*/*-pld-linux-thread-multi/auto/Apache/TS/.packlist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/perl5/*/*-pld-linux-thread-multi/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{_datadir}/perl5/Apache/TS.pm.in

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%attr(755,root,root) %{_bindir}/traffic_cop
%attr(755,root,root) %{_bindir}/traffic_line
%attr(755,root,root) %{_bindir}/traffic_logcat
%attr(755,root,root) %{_bindir}/traffic_logstats
%attr(755,root,root) %{_bindir}/traffic_manager
%attr(755,root,root) %{_bindir}/traffic_sac
%attr(755,root,root) %{_bindir}/traffic_server
%attr(755,root,root) %{_bindir}/traffic_shell
%attr(755,root,root) %{_bindir}/traffic_top
%attr(755,root,root) %{_bindir}/trafficserver
%attr(755,root,root) %{_bindir}/tspush
%attr(755,root,root) %{_bindir}/tstop
%attr(755,root,root) %{_bindir}/tsxs
%{_docdir}/trafficserver/trafficshell/*.1
%{_mandir}/man1/*.1*
%{_mandir}/man3/TS*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

# libs
%attr(755,root,root) %{_libdir}/libtsmgmt.so.*.*.*
%ghost %{_libdir}/libtsmgmt.so.4
%attr(755,root,root) %{_libdir}/libtsmgmtshare.so.*.*.*
%ghost %{_libdir}/libtsmgmtshare.so.4
%attr(755,root,root) %{_libdir}/libtsutil.so.*.*.*
%ghost %{_libdir}/libtsutil.so.4

#%files devel
#%defattr(644,root,root,755)
%{_includedir}/ts
%{_libdir}/*.la
%{_libdir}/*.so

#%files -n perl-Apache-TS
#%defattr(644,root,root,755)
%{_datadir}/perl5/Apache/TS.pm
%{_datadir}/perl5/Apache/TS
%{_mandir}/man3/Apache::TS*.3pm*
