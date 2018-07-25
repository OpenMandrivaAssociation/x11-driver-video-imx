%define upname xserver-xorg-video-imx

Summary:   Xorg X11 I.MX driver
Name:      x11-driver-video-imx
Version:   11.09.01
Release:   8
URL:       http://freescale.com
License:   MIT
Group:     System/X11
Patch0:    Fix-error-unknown-type-name-uint.patch
Patch1:    Make-video-API-forward-and-backward-compatible.patch
Patch2:	   ext-Update-to-newer-swap-macros.patch
Patch3:    xf86-video-imxfb-fix-m4-hardcodded-paths.patch
Patch4:	   xserver-1.14-compat.patch

Source0:   http://archlinuxarm.org/builder/src/%{upname}-%{version}.tar.gz

ExclusiveArch: %{arm}

BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xorg-server)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(x11)

Requires:	udev

%description 
Driver for Freescale I.MX devices

%prep
%setup -qn %{upname}-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%doc README COPYING
%{_libdir}/xorg/modules/drivers/armsoc_drv.so
%{_mandir}/man4/armsoc.4*
