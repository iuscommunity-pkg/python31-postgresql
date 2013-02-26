%global __python31 /usr/bin/python3.1
%{!?python31_sitearch: %global python31_sitearch %(%{__python31} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python31-postgresql
Version:        1.1.0
Release:        1.ius%{?dist}
Summary:        Connect to PostgreSQL with Python 3

Group:          Applications/Databases
License:        BSD
URL:            http://python.projects.postgresql.org/
Source0:        http://pypi.python.org/packages/source/p/py-postgresql/py-postgresql-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python31-devel

%description
py-postgresql is a Python 3 package providing modules to work with PostgreSQL.
This includes a high-level driver, and many other tools that support a
developer working with PostgreSQL databases.

%prep
%setup -q -n py-postgresql-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python31} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python31} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{python31_sitearch}/*


%changelog
* Thu Oct 25 2012 Ben Harper <ben.harper@rackspace.com> 1.1.0-1.ius
- Latest Sources from Upstream
- Changed source to pypi per http://pgfoundry.org/pipermail/python-general/2012-October/001002.html

* Thu May 03 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.4-1.ius
- Latest Sources from Upstream

* Mon Apr 16 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.3-2.ius
- Rebuilding against latest python31

* Tue Oct 18 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.3-1.ius
- Latest Sources from Upstream

* Mon Jun 13 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.2-3.ius
- Rebuilding against latest python 3.1.4

* Tue May 31 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.2-2.ius
- Rebuilding against latest Python31 package

* Fri Apr 01 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.2-1.ius
- Latest Sources from Upstream

* Tue Feb 01 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.0-3.ius
- Porting from Fedora to IUS

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr  2 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial package

