%{?mingw_package_header}

%global pkgname minizip

Name:          mingw-%{pkgname}
Version:       2.10.2
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       zlib
URL:           https://github.com/nmoinvaz/%{pkgname}
Source0:       https://github.com/nmoinvaz/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Allow option to skip git clone for MZ_BRG
Patch0:        minizip-2.10.2-BRG_FORCE_FETCH.patch
# Rename gladmans shared libraries
Patch1:        minizip-2.10.2-rename-gladmans-shared-libraries.patch

BuildRequires: cmake

BuildRequires: mingw32-curl
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-xz
BuildRequires: mingw32-zlib
BuildRequires: mingw32-zstd

BuildRequires: mingw64-curl
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-xz
BuildRequires: mingw64-zlib
BuildRequires: mingw64-zstd


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
MINGW32_CMAKE_ARGS="-DINSTALL_INC_DIR=%{mingw32_includedir}/%{pkgname}" \
MINGW64_CMAKE_ARGS="-DINSTALL_INC_DIR=%{mingw64_includedir}/%{pkgname}" \
%mingw_cmake -DZSTD_FORCE_FETCH=OFF -DBRG_FORCE_FETCH=OFF
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/cmake/%{pkgname}/
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/cmake/%{pkgname}/
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/


%changelog
* Thu Nov 12 2020 Sandro Mani <manisandro@gmail.com> - 2.10.2-1
- Initial package
