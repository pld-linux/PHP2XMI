%include	/usr/lib/rpm/macros.php
Summary:	Produces XMI 1.3 schemes (UML) from PHP files
Name:		PHP2XMI
Version:	0.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://tech.motion-twin.com/zip/%{name}-%{version}.tar.gz
# Source0-md5:	42821db581216c3a91dec91e1987ea24
URL:		http://tech.motion-twin.com/php_php2xmi.html
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP2XMI produces XMI 1.3 schemes (UML) from PHP files.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install php2xmi $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*