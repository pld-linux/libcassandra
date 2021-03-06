
Summary:	A high level C++ client for Cassandra
Summary(pl.UTF-8):	Klient Cassandry wyższego poziomu w C++
Name:		libcassandra
Version:	0.2.91
Release:	5
License:	BSD
Group:		Libraries
# https://download.github.com/matkor-libcassandra-0.2.91-0-g98ab52b.tar.gz
Source0:	https://download.github.com/matkor-libcassandra-%{version}-0-g98ab52b.tar.gz
# Source0-md5:	8563f97a35ca4b465250e1e26873016e
# Patch0:		%{name}-link_fix.patch
Patch1:		%{name}-ac.patch
URL:		https://github.com/posulliv/libcassandra
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	thrift-devel >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ wrapper library for the interface to cassandra generated by
thrift. This library is based on the Java client hector.

%description -l pl.UTF-8
Biblioteak C++ wokół interfejsu do Cassandry wygnerwoanej przez
thrift. Oparta na Javowym kliencie Hector.


%package devel
Summary:	Header files for libcassandra library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcassandra
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	thrift-devel

%description devel
Header files for libcassandra library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcassandra.


%prep
%setup -q -n matkor-libcassandra-98ab52b
# %patch0 -p1
%patch1 -p1

%{__sed} -i -e 's|-Werror||g' m4/pandora_canonical.m4 m4/pandora_warnings.m4
%{__sed} -i -e 's|-O3||g' m4/pandora_optimize.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	acl_libdirstem=%{_lib} \
	CXXFLAGS="%{rpmcxxflags} -Wno-variadic-macros -Wno-deprecated"

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libcassandra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcassandra.so.3
%attr(755,root,root) %{_libdir}/libgenthrift.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgenthrift.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcassandra.so
%{_libdir}/libcassandra.la
%{_libdir}/libgenthrift.so
%{_libdir}/libgenthrift.la
%{_includedir}/libcassandra
%{_includedir}/libgenthrift
