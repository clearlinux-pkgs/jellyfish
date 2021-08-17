#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jellyfish
Version  : 0.8.8
Release  : 4
URL      : https://files.pythonhosted.org/packages/76/88/e6eba0ebd8a11eb0a03392d827f0a605ad45fbb24234f7db98ca1ecb41b2/jellyfish-0.8.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/76/88/e6eba0ebd8a11eb0a03392d827f0a605ad45fbb24234f7db98ca1ecb41b2/jellyfish-0.8.8.tar.gz
Summary  : a library for doing approximate and phonetic matching of strings.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jellyfish-license = %{version}-%{release}
Requires: jellyfish-python = %{version}-%{release}
Requires: jellyfish-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=========
jellyfish
=========
.. image:: https://github.com/jamesturk/jellyfish/workflows/Python%20package/badge.svg

%package license
Summary: license components for the jellyfish package.
Group: Default

%description license
license components for the jellyfish package.


%package python
Summary: python components for the jellyfish package.
Group: Default
Requires: jellyfish-python3 = %{version}-%{release}

%description python
python components for the jellyfish package.


%package python3
Summary: python3 components for the jellyfish package.
Group: Default
Requires: python3-core
Provides: pypi(jellyfish)

%description python3
python3 components for the jellyfish package.


%prep
%setup -q -n jellyfish-0.8.8
cd %{_builddir}/jellyfish-0.8.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629233987
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jellyfish
cp %{_builddir}/jellyfish-0.8.8/LICENSE %{buildroot}/usr/share/package-licenses/jellyfish/48ab590f8913118bda3509d03513168c0543422e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jellyfish/48ab590f8913118bda3509d03513168c0543422e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
