%define upstream_name    Net-Traceroute
%define upstream_version 1.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.14
Release:	1

Summary:	Net-Traceroute module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-Traceroute-1.14.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements traceroute(1) functionality for perl5. It
allows you to trace the path IP packets take to a destination. It
is currently implemented as a parser around the system traceroute
command.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags}"

%check
# make test dies...
# make test

%install
%makeinstall_std

%files
%doc ChangeLog README TODO
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.130.0-2mdv2011.0
+ Revision: 657455
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.130.0-1
+ Revision: 638932
- update to new version 1.13

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 629499
- update to new version 1.12

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 628737
- update to new version 1.11

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 404260
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.10-4mdv2009.0
+ Revision: 258137
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.10-3mdv2009.0
+ Revision: 246201
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.1
+ Revision: 97525
- update to new version 1.10

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.09-4mdv2008.0
+ Revision: 25453
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.09-3mdv2008.0
+ Revision: 25194
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.09-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL
- use mkrel

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.09-1mdk
- 1.09

* Thu Feb 10 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.08-1mdk
- initial Mandrakelinux package


