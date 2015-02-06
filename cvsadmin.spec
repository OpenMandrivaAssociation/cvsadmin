%define	name	cvsadmin
%define	version	1.0.3
%define release	12

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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-11mdv2011.0
+ Revision: 610183
- rebuild

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.3-10mdv2010.1
+ Revision: 502927
- fix licence, URL, clean spec file

* Tue Dec 08 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.3-9mdv2010.1
+ Revision: 474900
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-7mdv2009.0
+ Revision: 243835
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.3-5mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cvsadmin


* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 1.0.3-5mdv2007.0
- rebuild

* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.0.3-4mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.3-3mdk
- rebuild

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.3-2mdk
- rebuild

* Thu Oct 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.3-1mdk
- 1.0.3

* Fri Nov 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2

* Mon Jun 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- updated to 1.0.1

* Tue Feb 13 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.7.4-1mdk
- updated to 0.7.4

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.7-2mdk 
- rebuild

* Mon Nov 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7-1mdk
- updated to 0.7

* Thu Oct 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- new in contribs
