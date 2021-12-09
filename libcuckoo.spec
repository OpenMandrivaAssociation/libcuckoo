%define devname %mklibname cuckoo -d

Name: libcuckoo
Version: 0.3
Release: 1
Source0: https://github.com/efficient/libcuckoo/archive/refs/tags/v%{version}.tar.gz
Summary: Hash table that allows multiple concurrent reader and writer threads
URL: https://github.com/efficient/libcuckoo
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake ninja
# This is a headers-only library
BuildArch: noarch

%description
libcuckoo provides a high-performance, compact hash table that allows multiple
concurrent reader and writer threads.

%package -n %{devname}
Summary: Hash table that allows multiple concurrent reader and writer threads
Group: Development/C

%description -n %{devname}
libcuckoo provides a high-performance, compact hash table that allows multiple
concurrent reader and writer threads.

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_datadir}/cmake/*
