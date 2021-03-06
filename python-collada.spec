%global realname pycollada

Name:           python-collada
Version:        0.4
Release:        3%{?dist}
Summary:        A python module for creating, editing and loading COLLADA
Group:          Development/Languages

License:        BSD
URL:            https://github.com/pycollada/pycollada
# https://github.com/pycollada/pycollada/archive/v0.4.tar.gz
Source0:        %{realname}-%{version}.tar.gz
# Disable pypi downloads in setup.py to guarantee use of only system libs
Patch0:         python-collada-0.4-disable_unittest_downloads.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# unit test requirements
BuildRequires:  python-dateutil
BuildRequires:  python-unittest2
BuildRequires:  numpy

Requires:       python-dateutil
Requires:       numpy


%description
pycollada is a python module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.


%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1 -z .no_downloads


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%check
%{__python} setup.py test


%files
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown
%{python_sitelib}/*


%changelog
* Sat Mar  9 2013 John Morris <john@zultron.com> - 0.4-3
- Rename disable_unittest_downloads patch to silence fedora-review
  warning and add patch description in a comment

* Fri Jan 25 2013 John Morris <john@zultron.com> - 0.4-2
- Add check section
- Add extra BRs for check and build
- Remove unneeded python site{lib,arch} macros

* Wed Jan 23 2013 Richard Shaw <hobbes1069@gmail.com> - 0.4-1
- Initial packaging.
