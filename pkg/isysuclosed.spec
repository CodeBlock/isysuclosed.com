%global gitdate 20180220
%global buildhost %(hostname)

Name:           isysuclosed
Version:        0.4.8
Release:        1.%{gitdate}git%{?dist}
Summary:        The "isysuclosed.com" webapp.
License:        BSD
URL:            https://github.com/relrod/isysuclosed.com
BuildRequires:  git ghc systemd chrpath

# This is disabled for my local builds, since I use cabal from git.
%if "%{buildhost}" != "t520.home.elrod.me"
BuildRequires: cabal-install >= 1.18
%endif

%description
Haskell (Scotty) app for isysuclosed.com

%prep
if [ -d isysuclosed.com ]; then
  cd isysuclosed.com
  git reset --hard && git pull
else
  git clone git://github.com/relrod/isysuclosed.com/
  cd isysuclosed.com
fi

%build
export LANG=en_US.UTF-8
cd isysuclosed.com
sed -i 's/-O0/-O2/' isysuclosed.cabal
cabal sandbox init
cabal install -j --only-dependencies
cabal install -j

%check

%install
mkdir -p %{buildroot}/%{_bindir}
cd isysuclosed.com
cp .cabal-sandbox/bin/%{name} %{buildroot}/%{_bindir}/%{name}
chrpath --delete %{buildroot}/%{_bindir}/%{name}

# API conf (not stored in repo)
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
touch %{buildroot}/%{_sysconfdir}/%{name}/wunderground_api_key

# systemd
mkdir -p %{buildroot}/%{_unitdir}
cp pkg/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service

%files
#%config(noreplace) %{_sysconfdir}/httpd/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/wunderground_api_key
%{_unitdir}/%{name}.service
%{_bindir}/%{name}

%changelog
* Tue Feb 20 2018 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.8-1.20180220git
- Deploy with -threaded

* Wed Feb 07 2018 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.7-1.20180207git
- Emergency deploy (unreported closing)

* Fri Jan 12 2018 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.7-1.20180112git
- Deploy

* Fri Jan 12 2018 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.6-1.20180112git
- Deploy

* Sat Jan 07 2017 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.5-1.20170107git
- Deploy

* Sat Jan 07 2017 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.4-1.20170107git
- Deploy

* Wed Aug 24 2016 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.3-1.20160824git
- Deploy

* Mon Apr 25 2016 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.2-1.20160425git
- Deploy

* Tue Feb 16 2016 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.1.1-1.20160216git
- Deploy

* Sun Jan 10 2016 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.1.0-1.20160110git
- Deploy

* Thu Dec 17 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.0.1-1.20151217git
- Deploy

* Tue Dec 1 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.4.0.0-1.20151201git
- Deploy

* Mon Nov 30 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.3.3.0-1.20151130git
- Deploy

* Tue Nov 10 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.3.2.0-1.20151110git
- Deploy

* Mon Nov 09 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.3.1.0-1.20151109git
- Deploy

* Mon Nov 09 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.3.0.0-1.20151109git
- Deploy

* Mon Feb 02 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.3.2-1.20150202git
- Deploy

* Sun Feb 01 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.3.1-1.20150201git
- Deploy

* Sun Feb 01 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.3.0-1.20150201git
- Deploy

* Thu Jan 08 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.2.1-2.20150108git
- Deploy

* Thu Jan 08 2015 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.2.0-1.20150108git
- Deploy

* Tue Nov 25 2014 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.1.0-1.20141125git
- Deploy

* Mon Nov 24 2014 Ricky Elrod <rbelrod@student.ysu.edu> - 0.2.0.0-1.20141124git
- Deploy

* Fri Oct 24 2014 Ricky Elrod <rbelrod@student.ysu.edu> - 0.1.0.0-1.20141024git
- Initial build
