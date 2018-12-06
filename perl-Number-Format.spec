#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Number-Format
Version  : 1.75
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/W/WR/WRW/Number-Format-1.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/W/WR/WRW/Number-Format-1.75.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnumber-format-perl/libnumber-format-perl_1.75-1.debian.tar.xz
Summary  : 'Perl extension for formatting numbers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

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

%description dev
dev components for the perl-Number-Format package.


%prep
%setup -q -n Number-Format-1.75
cd ..
%setup -q -T -D -n Number-Format-1.75 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Number-Format-1.75/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Number/Format.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::Format.3
