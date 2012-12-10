%define name	listadmin
%define version	2.40
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Command line mailman interface
Url:		http://heim.ifi.uio.no/kjetilho/hacks/#listadmin
Source:		http://heim.ifi.uio.no/kjetilho/hacks/%{name}-%{version}.tar.gz
License:	GPL
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
listadmin is a command-line alternative to Mailman's Web interface for
administering mailing lists. It allows you to inspect messages or subscription
requests, approve or discard them manually, or discard messages automatically
when certain conditions are true. listadmin can also be configured to run out
of cron to do routine cleaning.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.40-6mdv2011.0
+ Revision: 620245
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.40-5mdv2010.0
+ Revision: 429858
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 2.40-4mdv2009.0
+ Revision: 251191
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 2.40-2mdv2008.1
+ Revision: 109218
- rebuild for new lzma

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.40-1mdv2008.1
+ Revision: 104461
- new version


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.37-1mdv2007.0
+ Revision: 120978
- new version

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2007.1
+ Revision: 111571
- Import listadmin

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2007.1
- first mdv release

