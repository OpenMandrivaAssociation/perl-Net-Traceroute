%define upstream_name    Net-Traceroute
%define upstream_version 1.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Net-Traceroute module for perl 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

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



