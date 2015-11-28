%define		module	dbfpy

Summary:	Module for accessing .DBF (dBase) files
Summary(pl.UTF-8):	Moduł pozwalajacy na dostęp do plików .DBF (dBase)
Name:		python-%{module}
Version:	2.2.4
Release:	2
License:	Public Domain
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/dbfpy/%{module}-%{version}.tar.gz
# Source0-md5:	1462be16a2c3d9afcca55a981bf2d75d
URL:		http://dbfpy.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbfpy is a python-only module for reading and writing DBF-files. It
was created by Jeff Kunce and then modified by Hans Fiby and Yaroslav
Samchuk.

%description -l pl.UTF-8
dbfpy to czysto pythonowy moduł do odczytu i zapisu plików DBF. Został
stworzony przez Jeffa Kunce, a następnie zmodyfikowany przez Hansa
Fiby'ego i Yaroslava Samchuka.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%dir %{py_sitescriptdir}/dbfpy
%{py_sitescriptdir}/dbfpy/*.py[co]
%{py_sitescriptdir}/*.egg-info
