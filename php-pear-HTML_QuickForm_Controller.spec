%define		_class		HTML
%define		_subclass	QuickForm
%define		upstream_name	%{_class}_%{_subclass}_Controller

Name:		php-pear-%{upstream_name}
Version:	1.0.10
Release:	5
Summary:	Add-on to HTML_QuickForm that allows building of multiple forms 
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_QuickForm_Controller/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package is essentially an implementation of a PageController
pattern. 

Architecture:
- Controller class that examines HTTP requests and manages form values
  persistance across requests.
- Page class (subclass of QuickForm) representing a single page of the
  form.
- Business logic is contained in subclasses of Action class.

Cool features:
- Includes several default actions that allows easy building of
  multipage forms.
- Includes usage examples for common usage cases (single-page form,
  wizard tabbed form).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-3mdv2011.0
+ Revision: 667505
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdv2011.0
+ Revision: 607105
- rebuild

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-1mdv2010.1
+ Revision: 489151
- update to new version 1.0.10

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-4mdv2010.1
+ Revision: 477873
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.9-3mdv2010.0
+ Revision: 426641
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-2mdv2009.1
+ Revision: 321857
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-1mdv2009.0
+ Revision: 272588
- 1.0.9

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.8-3mdv2009.0
+ Revision: 224741
- rebuild

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-2mdv2008.1
+ Revision: 166134
- rpmlint fixes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-1mdv2008.0
+ Revision: 28895
- 1.0.8

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-1mdv2008.0
+ Revision: 15539
- 1.0.7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2007.0
+ Revision: 81103
- Import php-pear-HTML_QuickForm_Controller

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1mdk
- 1.0.5

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdk
- initial Mandriva package (PLD import)

