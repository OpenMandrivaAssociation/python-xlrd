%define module	xlrd

Name:		python-%{module}
Version:	2.0.2
Release:	1
Summary:	Module for extracting data from MS Excel spreadsheets in Python
License:	BSD
Group:		Development/Python
URL:		https://pypi.python.org/pypi/xlrd/
Source0:	https://files.pythonhosted.org/packages/source/x/%{module}/%{module}-%{version}.tar.gz
BuildSystem:		python
BuildArch:			noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	dos2unix

%description
a library for reading data and formatting information
from Excel files in the historical .xls format.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

for i in */*.py; do
  # fix missing files
  dos2unix $i || :
done

%build
%py_build

%install
%py_install
mv -f %{buildroot}%{_bindir}/runxlrd.py %{buildroot}%{_bindir}/runxlrd

%files
%doc README.rst
%license LICENSE
%{_bindir}/run%{module}
%{python_sitelib}/xlrd
%{python_sitelib}/%{module}-%{version}*.*-info
