Summary:	Net6 network library
Summary(pl.UTF-8):	Biblioteka sieciowa net6
Name:		net6
Version:	1.3.14
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://releases.0x539.de/net6/%{name}-%{version}.tar.gz
# Source0-md5:	be6db739f71c5c08421bf6181e77f3b2
Patch0:		%{name}-gnutls.patch
Patch1:		long-long.patch
URL:		https://gobby.github.io/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.15
BuildRequires:	gnutls-devel >= 2.2
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
net6 is a library which eases the development of network-based
applications as it provides a TCP protocol abstraction for C++. It is
portable to both the Windows and Unix-like platforms.

%description -l pl.UTF-8
net6 to biblioteka ułatwiająca tworzenie aplikacji sieciowych,
udostępniająca abstrakcję protokołu TCP dla C++. Jest przenośna na
platformy uniksowe oraz Windows.

%package devel
Summary:	Header files for net6
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki net6
Summary(pt_BR.UTF-8):	Arquivos do pacote net6 para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel >= 2.2
Requires:	libsigc++-devel >= 2.0

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
%patch -P0 -p1
%patch -P1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnet6.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libnet6-1.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnet6-1.3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnet6.so
%{_includedir}/net6
%{_pkgconfigdir}/net6-1.3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnet6.a
