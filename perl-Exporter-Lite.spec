#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Exporter
%define	pnam	Lite
Summary:	Exporter::Lite - lightweight exporting of variables
Summary(pl):	Exporter::Lite - lekkie eksportowanie zmiennych
Name:		perl-Exporter-Lite
Version:	0.01
Release:	2
# contains "same as perl" modules for tests
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e45c93513ecb22e183748592069bdaf8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports import(), @EXPORT and
@EXPORT_OK and not a whole lot else.

Unlike Exporter, it is not necessary to inherit from Exporter::Lite
(ie. no @ISA = qw(Exporter::Lite) mantra).  Exporter::Lite simply
exports its import() function.  This might be called a "mix-in".

%description -l pl
Ten modu³ jest alternatyw± dla Exportera maj±c± udostêpniæ lekki
podzbiór jego funkcjonalno¶ci. Obs³uguje import(), @EXPORT oraz
@EXPORT_OK i niewiele wiêcej.

W przeciwieñstwie do Exportera, nie trzeba dziedziczyæ z
Exporter::Lite (czyli wykonywaæ mantry @ISA = qw(Exporter::Lite)).
Exporter::Lite po prostu eksportuje swoj± funkcjê import(). Mo¿na
to nazwaæ "miksowaniem".

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
