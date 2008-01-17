Summary:	Net6 network library
Summary(pl.UTF-8):	Biblioteka sieciowa net6
Name:		net6
Version:	1.3.4
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://releases.0x539.de/net6/%{name}-%{version}.tar.gz
# Source0-md5:	3e6a5bbe1d6fc8d0a3c295323114cbb0
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net6 network library.

%description -l pl.UTF-8
Biblioteka sieciowa net6.

%package devel
Summary:	Header files for net6
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki net6
Summary(pt_BR.UTF-8):	Arquivos do pacote net6 para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsigc++-devel

%description devel
Header files for net6.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki net6.

%description devel -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam net6.

%package static
Summary:	Static net6 library
Summary(pl.UTF-8):	Biblioteka statyczna net6
Summary(pt_BR.UTF-8):	Arquivos do pacote net6 para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static net6 library.

%description static -l pl.UTF-8
Biblioteka statyczna net6.

%description static -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam net6.

%prep
%setup -q

%build
rm -f *.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
