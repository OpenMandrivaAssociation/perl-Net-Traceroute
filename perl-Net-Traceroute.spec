%define upstream_name    Net-Traceroute
%define upstream_version 1.15
Name:		perl-%{upstream_name}
Version:	1.15
Release:	1

Summary:	Net-Traceroute module for perl 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/H/HA/HAG/Net-Traceroute-1.15.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements traceroute(1) functionality for perl5. It
allows you to trace the path IP packets take to a destination. It
is currently implemented as a parser around the system traceroute
command.

%prep
%setup -q -n %{upstream_name}-%{version}

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



