%define		module	dbfpy

Summary:	Module for accessing .DBF (dBase) files
Name:		python-%{module}
Version:	2.1.0
Release:	0.1
License:	public domain
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/dbfpy/%{module}-%{version}.tar.gz
# Source0-md5:	a0f2acf9ce8c7d794f59c533d2d8db18
URL:		http://dbfpy.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbfpy is a python-only module for reading and writing DBF-files. It was created
by Jeff Kunce and then modified by Hans Fiby and Yaroslav Samchuk.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitescriptdir}/dbfpy/*.py[co]
%{py_sitescriptdir}/*.egg-info
