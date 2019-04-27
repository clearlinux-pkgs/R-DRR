#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DRR
Version  : 0.0.3
Release  : 21
URL      : https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz
Summary  : Dimensionality Reduction via Regression
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-CVST
BuildRequires : R-kernlab
BuildRequires : buildreq-R

%description
# DRR
[![Travis Build Status](https://travis-ci.org/gdkrmr/DRR.svg?branch=master)](https://travis-ci.org/gdkrmr/DRR)
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/DRR)](https://cran.r-project.org/package=DRR)

%prep
%setup -q -c -n DRR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552955917

%install
export SOURCE_DATE_EPOCH=1552955917
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DRR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DRR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DRR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  DRR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DRR/DESCRIPTION
/usr/lib64/R/library/DRR/INDEX
/usr/lib64/R/library/DRR/LICENSE
/usr/lib64/R/library/DRR/Meta/Rd.rds
/usr/lib64/R/library/DRR/Meta/features.rds
/usr/lib64/R/library/DRR/Meta/hsearch.rds
/usr/lib64/R/library/DRR/Meta/links.rds
/usr/lib64/R/library/DRR/Meta/nsInfo.rds
/usr/lib64/R/library/DRR/Meta/package.rds
/usr/lib64/R/library/DRR/Meta/vignette.rds
/usr/lib64/R/library/DRR/NAMESPACE
/usr/lib64/R/library/DRR/R/DRR
/usr/lib64/R/library/DRR/R/DRR.rdb
/usr/lib64/R/library/DRR/R/DRR.rdx
/usr/lib64/R/library/DRR/doc/comparePCA.R
/usr/lib64/R/library/DRR/doc/comparePCA.Rmd
/usr/lib64/R/library/DRR/doc/comparePCA.html
/usr/lib64/R/library/DRR/doc/index.html
/usr/lib64/R/library/DRR/help/AnIndex
/usr/lib64/R/library/DRR/help/DRR.rdb
/usr/lib64/R/library/DRR/help/DRR.rdx
/usr/lib64/R/library/DRR/help/aliases.rds
/usr/lib64/R/library/DRR/help/paths.rds
/usr/lib64/R/library/DRR/html/00Index.html
/usr/lib64/R/library/DRR/html/R.css
