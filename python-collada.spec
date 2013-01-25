# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global realname pycollada

Name:           python-collada
Version:        0.4
Release:        1%{?dist}
Summary:        A python module for creating, editing and loading COLLADA

License:        BSD
URL:            https://github.com/pycollada/pycollada
# https://github.com/pycollada/pycollada/archive/v0.4.tar.gz
Source0:        %{realname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel

%description
pycollada is a python module for creating, editing and loading COLLADA, which
is a COLLAborative Design Activity for establishing an interchange file format
for interactive 3D applications.

The library allows you to load a COLLADA file and interact with it as a python
object. In addition, it supports creating a collada python object from scratch,
as well as in-place editing.


%prep
%setup -q -n %{realname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%files
%doc AUTHORS.md CHANGELOG.rst COPYING README.markdown
%{python_sitelib}/*


%changelog
* Wed Jan 23 2013 Richard Shaw <hobbes1069@gmail.com> - 0.4-1
- Initial packaging.
