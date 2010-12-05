%define	name	cvsadmin
%define	version	1.0.3
%define	release	%mkrel 11

Version:	%{version}
Summary:	Tool to administer users of a CVS repository
Name:		%{name}
Release:	%{release}
License:	GPLv2
Group:		Development/Other
Source:		%{name}-%{version}.tar.bz2
URL:		ftp://ftp.freebsd.org/pub/FreeBSD/ports/local-distfiles/gabor/
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
cvsadmin is a simple program to administrate users of a CVS repository. 

It currently allows you to easily
- add users
- remove users
- change users passwords
- show existing users
- rename users
- change system users

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS COPYING Makefile README 
%{_bindir}/*

