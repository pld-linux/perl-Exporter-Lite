#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Exporter
%define		pnam	Lite
Summary:	Exporter::Lite - lightweight exporting of variables
Summary(pl.UTF-8):	Exporter::Lite - lekkie eksportowanie zmiennych
Name:		perl-Exporter-Lite
Version:	0.02
Release:	1
# contains "same as perl" modules for tests
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e2ed5978a09020de16b5cf30c84566b0
URL:		http://search.cpan.org/dist/Exporter-Lite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality. It supports import(), @EXPORT and
@EXPORT_OK and not a whole lot else.

Unlike Exporter, it is not necessary to inherit from Exporter::Lite
(ie. no @ISA = qw(Exporter::Lite) mantra). Exporter::Lite simply
exports its import() function. This might be called a "mix-in".

%description -l pl.UTF-8
Ten moduł jest alternatywą dla Exportera mającą udostępnić lekki
podzbiór jego funkcjonalności. Obsługuje import(), @EXPORT oraz
@EXPORT_OK i niewiele więcej.

W przeciwieństwie do Exportera, nie trzeba dziedziczyć z
Exporter::Lite (czyli wykonywać mantry @ISA = qw(Exporter::Lite)).
Exporter::Lite po prostu eksportuje swoją funkcję import(). Można to
nazwać "miksowaniem".

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
