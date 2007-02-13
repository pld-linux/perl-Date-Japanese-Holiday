#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Japanese-Holiday
Summary:	Date::Japanese::Holiday - calculate dates in the Japanese-Holiday calendar
Summary(pl.UTF-8):	Date::Japanese::Holiday - obliczanie daty wg japońskiego kalendarza świąt
Name:		perl-Date-Japanese-Holiday
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b0bed78ad2127afe06f01f346caa36e
BuildRequires:	perl-Date-Simple
BuildRequires:	perl-Time-modules
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Japanese::Holiday handles conversion between Japanese Holiday and
Gregorian calendar.

%description -l pl.UTF-8
Date::Japanese::Holiday obsługuje konwersję dat pomiędzy japońskimi
swiętami a kalendarzem gregoriańskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Date/Japanese/Holiday.pm
%{_mandir}/man3/*
