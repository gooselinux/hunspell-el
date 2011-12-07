Name: hunspell-el
Summary: Greek hunspell dictionaries
Epoch: 1
Version: 0.7
Release: 5%{?dist}
Source: http://ispell.math.upatras.gr/files/ooffice/el_GR.zip
Group: Applications/Text
URL: http://ispell.math.upatras.gr/?section=oofficespell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPL
BuildArch: noarch

Requires: hunspell

%description
Greek hunspell dictionaries.

%prep
%setup -q -c -n hunspell-el

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s el_GR.aff $lang.aff
        ln -s el_GR.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_el_GR.txt
%{_datadir}/myspell/*

%changelog
* Fri Jun 11 2010 Caolán McNamara <caolanm@redhat.com> - 1:0.7-5
- Resolves: rhbz#602263 clarify licence

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:0.7-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.7-3
- extend coverage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.7-1
- latest upstream version
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20041220-1
- initial version
