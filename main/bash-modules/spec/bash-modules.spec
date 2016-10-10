
Name:           bash-modules
Version:        3.0.0
Release:        1%{?dist}
Summary:        Modules for bash

Group:          System Environment/Libraries
URL:            https://github.com/vlisivka/bash-modules
License:        LGPL-2.1+
Source0:        %{name}.tar.gz
BuildArch:      noarch

%define  homedir /usr/share/bash-modules

%description
Optional modules to use with bash, like logging, argument parsing, etc.

%prep
%setup -q -n %{name}

%build
# Nothing to do

# Execute tests
#(
#  cd test
#  exec /bin/bash ./test.sh -q
#)

%install
install -D src/import.sh "$RPM_BUILD_ROOT%_bindir/import.sh"

mkdir -p "$RPM_BUILD_ROOT%homedir/"
cp -a src/bash-modules/* "$RPM_BUILD_ROOT%homedir/"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc COPYING* README Changelog doc/

%attr(0755,root,root) %_bindir/import.sh
%homedir


%changelog
* Thu Apr 8 2016 Volodymyr M. Lisivka <vlisivka@gmail.com> - 2.0.4-1
- Dependency on perl (for documentation) is removed.

* Wed Jul 31 2013 Volodymyr M. Lisivka <vlisivka@gmail.com> - 2.0.2-4
- Group changed again from to "System/Libraries"
- URL to home page is changed to github

* Mon Jul 29 2013 Volodymyr M. Lisivka <vlisivka@gmail.com> - 2.0.2-3
- Group changed from "System Environment/Base" to "Development/Libraries/Bash"

* Tue Jul 16 2013 Volodymyr M. Lisivka <vlisivka@gmail.com> - 2.0.2-2
- License tag changed from LGPL to LGPL2.1+
