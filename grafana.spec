Name:		grafana
Version:	1.9.0
Release:	1kaji0.2
Summary:	Graphite & InfluxDB Dashboard and Graph Editor

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/grafana
Source0:	%{name}_%{version}.orig.tar.gz
BuildArch:  noarch


%description
Graphite & InfluxDB Dashboard and Graph Editor
Grafana is An open source, feature rich metrics dashboard and
graph editor for Graphite, InfluxDB & OpenTSDB.

%prep
%setup -q

for patch_file in $(grep -v "^#" debian/patches/series)
do
%{__patch} -p1 < debian/patches/$patch_file
done

%build


%install
rm -rf %{buildroot}/*



install -d %{buildroot}/usr/share/grafana/
install -dpm0755 app %{buildroot}/usr/share/grafana/ 
install -pm0755 build.txt %{buildroot}/usr/share/grafana/ 
install -pm0755 config.sample.js %{buildroot}/usr/share/grafana/ 
install -pm0755 config.js %{buildroot}/usr/share/grafana/ 
install -dpm0755 css %{buildroot}/usr/share/grafana/ 
install -dpm0755 font %{buildroot}/usr/share/grafana/ 
install -dpm0755 img %{buildroot}/usr/share/grafana/ 
install -pm0755 index.html %{buildroot}/usr/share/grafana/ 
install -pm0755 LICENSE.md %{buildroot}/usr/share/grafana/ 
install -pm0755 NOTICE.md %{buildroot}/usr/share/grafana/ 
install -dpm0755 plugins %{buildroot}/usr/share/grafana/ 
install -pm0755 README.md %{buildroot}/usr/share/grafana/ 
install -dpm0755 test %{buildroot}/usr/share/grafana/ 
install -dpm0755 vendor %{buildroot}/usr/share/grafana/ 


install -d %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -pm0755 grafana.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/grafana.conf

%files
/usr/share/grafana/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/grafana.conf


%changelog
* Wed Jan 21 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 1.9.0-1kaji0.2
- Initial Package
