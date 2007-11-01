%define name	listadmin
%define version	2.40
%define release	%mkrel 1

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


