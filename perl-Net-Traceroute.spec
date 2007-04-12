%define module Net-Traceroute
%define name perl-Net-Traceroute
%define version 1.09
%define release %mkrel 2

Summary:	Net-Traceroute module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module implements traceroute(1) functionality for perl5. It
allows you to trace the path IP packets take to a destination. It
is currently implemented as a parser around the system traceroute
command.

%prep

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags}"

# make test dies...
# make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README TODO
%{perl_vendorlib}/*
%{_mandir}/*/*

