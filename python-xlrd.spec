%define module	xlrd
%define name  	python-%{module}
%define version 0.8.0
%define release 1

Summary:	Module for extracting data from MS Excel spreadsheets in Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/x/%{module}/%{module}-%{version}.tar.gz
Source1:	runxlrd.py
License:	BSD 
Group:		Development/Python 
Url:		http://pypi.python.org/pypi/xlrd/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
%py_requires -d

%description
Extract data from new and old Excel spreadsheets on any platform. Pure
Python (2.1 to 2.6). Strong support for Excel dates. Unicode-aware.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mv %{buildroot}%{py_sitedir}/xlrd/doc/* .
%__cp -f %{SOURCE1} %{buildroot}%{_bindir}
%__chmod 755 %{buildroot}%{_bindir}/runxlrd*
%__rm -rf %{buildroot}%{py_sitedir}/xlrd/doc/
%__mv %{buildroot}%{py_sitedir}/xlrd/examples .
%__mv %{buildroot}%{_bindir}/runxlrd.py %{buildroot}%{_bindir}/runxlrd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.html examples 
%_bindir/runxlrd
%py_sitedir/xlrd*

