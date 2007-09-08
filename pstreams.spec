Summary:	PStreams - POSIX Process Control in C++
Summary(pl.UTF-8):	PStreams - sterowanie POSIX-owymi procesami w C++
Name:		pstreams
Version:	0.5.2
Release:	1
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/pstreams/%{name}-%{version}.tar.gz
# Source0-md5:	d8a9bd488f3e7b75feabc7b136ad8be0
URL:		http://pstreams.sourceforge.net/
Requires:	libstdc++-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PStreams allows you to run another program from your C++ application
and to transfer data between the two programs similar to shell
pipelines.

%description -l pl.UTF-8
PStreams umożliwia uruchamianie innego programu z poziomu aplikacji w
C++ i przesyłanie danych między programami w sposób podobny do potoków
powłoki systemowej.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

install pstream.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README mainpage.html
%{_includedir}/pstream.h
