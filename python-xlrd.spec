%define module	xlrd

Summary:	Module for extracting data from MS Excel spreadsheets in Python


Name:		python-%{module}
Version:	0.9.4
Release:	1
Source0:	http://pypi.python.org/packages/source/x/xlrd/xlrd-%{version}.tar.gz
License:	BSD 
Group:		Development/Python 
Url:		http://pypi.python.org/pypi/xlrd/
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	dos2unix

BuildRequires:  python-devel

%description
Extract data from new and old Excel spreadsheets on any platform. 
Pure Python. Strong support for Excel dates. Unicode-aware.

%prep
%setup -q -n %{module}-%{version}
for i in */*.py *.html; do
  # fix missing files
  dos2unix $i || :
done

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

# fix linting, add shebang,fix extentions in _bindir
(
  echo '#!%{__python}'
  cat %{buildroot}%{_bindir}/runxlrd.py
) >> %{buildroot}%{_bindir}/runxlrd
rm -rf %{buildroot}%{_bindir}/runxlrd.py* \
  %{buildroot}/%{py_puresitedir}/xlrd/doc \
  %{buildroot}/%{py_puresitedir}/xlrd/examples 


%files
%attr(755,root,root) %dir %{py_puresitedir}/xlrd
%{py_puresitedir}/xlrd/*
%{py_puresitedir}/*egg-info
%attr(755,root,root) %{_bindir}/*



