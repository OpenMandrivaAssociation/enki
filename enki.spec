#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/enki enki; \
#cd enki; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf enki-$PKG_VERSION.tar.xz enki/ --exclude .svn --exclude .*ignore

%define svnrev  66410

Summary:	Enki Photo Manager for E17
Name:		enki
Version:	0.6.0
Release:	0.%{svnrev}.1
License:	GPLv2
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz
Patch0:		enki-desktop.patch

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(enlil)
BuildRequires:	pkgconfig(elementary)

Requires:	enlil

%description
Enki is a photo manager using the EFL and allows the user to manage a
list of albums and photos.

%prep
%setup -qn %{name}
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x 
%make

%install
rm -fr %{buildroot}
%makeinstall

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/enki
%{_bindir}/enki-slideshow
%{_datadir}/enki/themes/*.edj
%{_datadir}/applications/enki.desktop
%{_datadir}/pixmaps/enki.png

