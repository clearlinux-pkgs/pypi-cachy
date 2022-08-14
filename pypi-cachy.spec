#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cachy
Version  : 0.3.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/a0/0c/45b249b0efce50a430b8810ec34c5f338d853c31c24b0b297597fd28edda/cachy-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/0c/45b249b0efce50a430b8810ec34c5f338d853c31c24b0b297597fd28edda/cachy-0.3.0.tar.gz
Summary  : Cachy provides a simple yet effective caching library.
Group    : Development/Tools
License  : MIT
Requires: pypi-cachy-license = %{version}-%{release}
Requires: pypi-cachy-python = %{version}-%{release}
Requires: pypi-cachy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Cachy
#####
.. image:: https://travis-ci.org/sdispater/cachy.png
:alt: Cachy Build status
:target: https://travis-ci.org/sdispater/cachy

%package license
Summary: license components for the pypi-cachy package.
Group: Default

%description license
license components for the pypi-cachy package.


%package python
Summary: python components for the pypi-cachy package.
Group: Default
Requires: pypi-cachy-python3 = %{version}-%{release}

%description python
python components for the pypi-cachy package.


%package python3
Summary: python3 components for the pypi-cachy package.
Group: Default
Requires: python3-core
Provides: pypi(cachy)

%description python3
python3 components for the pypi-cachy package.


%prep
%setup -q -n cachy-0.3.0
cd %{_builddir}/cachy-0.3.0
pushd ..
cp -a cachy-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363312
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cachy
cp %{_builddir}/cachy-0.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cachy/98a929dd0a579b9761599bc34c800296ad986dcd
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cachy/98a929dd0a579b9761599bc34c800296ad986dcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
