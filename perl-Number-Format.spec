#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Number-Format
Version  : 1.76
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Number-Format-1.76.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Number-Format-1.76.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnumber-format-perl/libnumber-format-perl_1.75-1.debian.tar.xz
Summary  : 'Perl extension for formatting numbers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Number-Format-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Number::Format - Convert numbers to strings with pretty formatting
WHAT IS IT
Number::Format is a library for formatting numbers.  Functions are
provided for converting numbers to strings in a variety of ways, and
to convert strings that contain numbers back into numeric form.  The
output formats may include thousands separators - characters inserted
between each group of three characters counting right to left from the
decimal point.  The characters used for the decimal point and the
thousands separator come from the locale information or can be
specified by the user.

%package dev
Summary: dev components for the perl-Number-Format package.
Group: Development
Provides: perl-Number-Format-devel = %{version}-%{release}
Requires: perl-Number-Format = %{version}-%{release}

%description dev
dev components for the perl-Number-Format package.


%package perl
Summary: perl components for the perl-Number-Format package.
Group: Default
Requires: perl-Number-Format = %{version}-%{release}

%description perl
perl components for the perl-Number-Format package.


%prep
%setup -q -n Number-Format-1.76
cd %{_builddir}
tar xf %{_sourcedir}/libnumber-format-perl_1.75-1.debian.tar.xz
cd %{_builddir}/Number-Format-1.76
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Number-Format-1.76/deblicense/
pushd ..
cp -a Number-Format-1.76 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::Format.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
