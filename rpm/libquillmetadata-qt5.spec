# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       libquillmetadata-qt5

# >> macros
# << macros

Summary:    Qt based library for still image metadata manipulation
Version:    1.111111.0
Release:    0
Group:      System/Libraries
License:    LGPLv2
URL:        https://github.com/nemomobile/quillmetadata
Source0:    %{name}-%{version}.tar.bz2
Source100:  libquillmetadata-qt5.yaml
Requires:   qt5-plugin-imageformat-jpeg
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  fdupes
BuildRequires:  libjpeg-devel
BuildRequires:  fdupes

%description
A Qt based library which can access and edit Exif, XMP and IPTC
metadata for still images (currently only JPEG format), offering
transparent reconciliation between different metadata representations.


%package tests
Summary:    Qt based library for still image metadata manipulation - unit tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   testrunner-lite

%description tests
A Qt based library which can access and edit Exif, XMP and IPTC
metadata for still images (currently only JPEG format), offering
transparent reconciliation between different metadata representations.

This package includes the unit tests.


%package devel
Summary:    Qt based library for still image metadata manipulation - development headers
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
A Qt based library which can access and edit Exif, XMP and IPTC
metadata for still images (currently only JPEG format), offering
transparent reconciliation between different metadata representations.

This package includes the development headers.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%fdupes  %{buildroot}/%{_libdir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libquillmetadata-qt5.so.*
# >> files
# << files

%files tests
%defattr(-,root,root,-)
%{_datadir}/libquillmetadata-qt5-tests/*
%{_libdir}/libquillmetadata-qt5-tests/*
# >> files tests
# << files tests

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/quillmetadata-qt5/*
%{_libdir}/libquillmetadata-qt5.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.pc
# >> files devel
# << files devel
