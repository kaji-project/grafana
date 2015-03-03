Name:		grafana
Version:	1.9.0
Release:	1kaji0.2
Summary:	Graphite & InfluxDB Dashboard and Graph Editor

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/grafana
Source0:	%{name}_%{version}.orig.tar.gz
BuildArch:  noarch
Requires:  httpd


%description
Graphite & InfluxDB Dashboard and Graph Editor
Grafana is An open source, feature rich metrics dashboard and
graph editor for Graphite, InfluxDB & OpenTSDB.
his package install Grafana with a read-only user to InfluxDB


%package admin
Summary:   Graphite & InfluxDB Dashboard and Graph Editor (Admin)
Group:     Network
Requires:  httpd

%description admin
Graphite & InfluxDB Dashboard and Graph Editor
Grafana is An open source, feature rich metrics dashboard and
graph editor for Graphite, InfluxDB & OpenTSDB.
This package install Grafana with a read/write user to InfluxDB

%prep
%setup -q

for patch_file in $(grep -v "^#" debian/patches/series)
do
%{__patch} -p1 < debian/patches/$patch_file
done

%build


%install
rm -rf %{buildroot}/*


install -d %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}/usr/share/grafana/
install -d %{buildroot}/%{_sysconfdir}/grafana/
cp -r app %{buildroot}/usr/share/grafana/ 
install -pm0755 build.txt %{buildroot}/usr/share/grafana/ 
install -pm0755 config.sample.js %{buildroot}/usr/share/grafana/ 
install -pm0755 config.js %{buildroot}/usr/share/grafana/ 
cp -r css %{buildroot}/usr/share/grafana/ 
cp -r font %{buildroot}/usr/share/grafana/ 
cp -r img %{buildroot}/usr/share/grafana/ 
install -pm0755 index.html %{buildroot}/usr/share/grafana/ 
install -pm0755 LICENSE.md %{buildroot}/usr/share/grafana/ 
install -pm0755 NOTICE.md %{buildroot}/usr/share/grafana/ 
cp -r plugins %{buildroot}/usr/share/grafana/ 
install -pm0755 README.md %{buildroot}/usr/share/grafana/ 
cp -r test %{buildroot}/usr/share/grafana/ 
cp -r vendor %{buildroot}/usr/share/grafana/ 
ln -sf /usr/share/grafana/config.js %{buildroot}/%{_sysconfdir}/grafana/config.js
install -pm0755 grafana.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/grafana.conf

install -d %{buildroot}/usr/share/grafana-admin/
ln -sf /usr/share/grafana/app %{buildroot}/usr/share/grafana-admin/app
ln -sf /usr/share/grafana/build.txt %{buildroot}/usr/share/grafana-admin/build.txt
ln -sf /usr/share/grafana/config.sample.js %{buildroot}/usr/share/grafana-admin/config.sample.js
ln -sf /usr/share/grafana/css %{buildroot}/usr/share/grafana-admin/css
ln -sf /usr/share/grafana/font %{buildroot}/usr/share/grafana-admin/font
ln -sf /usr/share/grafana/img %{buildroot}/usr/share/grafana-admin/img
ln -sf /usr/share/grafana/index.html %{buildroot}/usr/share/grafana-admin/index.html
ln -sf /usr/share/grafana/LICENSE.md %{buildroot}/usr/share/grafana-admin/LICENSE.md
ln -sf /usr/share/grafana/NOTICE.md %{buildroot}/usr/share/grafana-admin/NOTICE.md
ln -sf /usr/share/grafana/plugins %{buildroot}/usr/share/grafana-admin/plugins
ln -sf /usr/share/grafana/README.md %{buildroot}/usr/share/grafana-admin/README.md
ln -sf /usr/share/grafana/test %{buildroot}/usr/share/grafana-admin/test
ln -sf /usr/share/grafana/vendor %{buildroot}/usr/share/grafana-admin/vendor
cp config_admin.js %{buildroot}/usr/share/grafana-admin/config.js
ln -sf /usr/share/grafana-admin/config.js %{buildroot}/%{_sysconfdir}/grafana/config-admin.js
install -pm0755 grafana-admin.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/grafana-admin.conf



%files
/usr/share/grafana/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/grafana.conf
%config(noreplace) %{_sysconfdir}/grafana/config.js


%files admin
/usr/share/grafana-admin/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/grafana-admin.conf
%config(noreplace) %{_sysconfdir}/grafana/config-admin.js

%changelog
* Wed Jan 21 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 1.9.0-1kaji0.2
- Initial Package
