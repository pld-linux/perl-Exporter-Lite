#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Exporter
%define	pnam	Lite
Summary:	Exporter::Lite - Lightweight exporting of variables
#Summary(pl):	
Name:		perl-Exporter-Lite
Version:	0.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports C<import()>, C<@EXPORT> and
C<@EXPORT_OK> and not a whole lot else.

Unlike Exporter, it is not necessary to inherit from Exporter::Lite
(ie. no C<@ISA = qw(Exporter::Lite)> mantra).  Exporter::Lite simply
exports its import() function.  This might be called a "mix-in".

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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
