Summary:	Authentication provider for mod_spin
Name:		spin_auth
Version:	1.1.6
Release:	%mkrel 2
Group:		System/Servers
License:	LGPLv2+
URL:		http://www.rexursive.com/software/modspin/applications.html
Source0:	ftp://ftp.rexursive.com/pub/spinapps/auth/%{name}-%{version}.tar.bz2
Requires:	apache-mod_spin >= 1.1.8
BuildRequires:	apache-devel
BuildRequires:	apache-mod_spin-devel >= 1.1.8
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	file
BuildRequires:	flex >= 2.5.33
BuildRequires:	libapreq-devel >= 2.07
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This mod_spin application provides authentication for other applications, using
some internal request trickery and session state. It is only valid for spin
macro files and it will not provide any protection against unauthorised access
to static (X)HTML or other types of files.

%prep

%setup -q -n %{name}-%{version}

%build
%serverbuild
libtoolize --copy --force --automake; aclocal -I m4; autoheader; autoconf; automake --add-missing --copy

%configure2_5x \
    --disable-static \
    --enable-packager \
    --libdir=%{_libdir}/spinapps

%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_sysconfdir}/httpd/modules.d
install -m0644 spin_auth.conf %{buildroot}%{_sysconfdir}/httpd/modules.d/A66_spin_auth.conf

# cleanup
rm -f %{buildroot}%{_libdir}/spinapps/spin_auth.*a
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/httpd/modules.d/A66_spin_auth.conf
%config(noreplace) %{_sysconfdir}/spinapps/spin_auth.xml
%{_libdir}/spinapps/spin_auth.so

