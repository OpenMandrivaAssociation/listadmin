Summary:	Command line mailman interface
Name:		listadmin
Version:	2.73
Release:	1
License:	Public Domain
Group:		File tools
Url:		https://sourceforge.net/projects/listadmin/
Source0:	https://sourceforge.net/projects/listadmin/files/%{version}/listadmin-%{version}.tar.gz
BuildArch:	noarch

%description
listadmin is a command-line alternative to Mailman's Web interface for
administering mailing lists. It allows you to inspect messages or subscription
requests, approve or discard them manually, or discard messages automatically
when certain conditions are true. listadmin can also be configured to run out
of cron to do routine cleaning.

%files
#{_bindir}/*
#{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make_build
%install
#install -d -m 755 %{buildroot}%{_bindir}
#install -d -m 755 %{buildroot}%{_mandir}/man1
%make_install
