Summary:	Skins for gDeskCal
Summary(pl.UTF-8):	Skórki dla gDeskCal
Name:		gDeskCal-skins
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/skins/gdeskcal/august.tar.gz
# Source0-md5:	74d9cb298532a16a68804102a4d89ef1
Source1:	http://www.pycage.de/download/skins/gdeskcal/gorillerat.tar.gz
# Source1-md5:	ee1b817bf5e8e338619851a0ef65c8fb
Source2:	http://www.pycage.de/download/skins/gdeskcal/grey_skin.tar.gz
# Source2-md5:	ae49b20ac9dda671f37958fda87cf005
Source3:	http://www.pycage.de/download/skins/gdeskcal/gnometheme.tar.gz
# Source3-md5:	b4571c365a82782b1819dc8cf1be7109
Source4:	http://www.pycage.de/download/skins/gdeskcal/SimpleForDark.tar.gz
# Source4-md5:	ead283c4139410e22f1e84b711381947
Source5:	http://www.pycage.de/download/skins/gdeskcal/e_01.tar.gz
# Source5-md5:	eb255e22d42056ee8fedf06bda62b3c2
Source6:	http://www.pycage.de/download/skins/gdeskcal/miderat_RTL.tar.gz
# Source6-md5:	52b17e482d33fa16a4d86c36e143f136
Source7:	http://www.pycage.de/download/skins/gdeskcal/light_01.tar.gz
# Source7-md5:	3113443a583893d928c156004d62f670
Source8:	http://www.pycage.de/download/skins/gdeskcal/light_02.tar.gz
# Source8-md5:	eb825f0f39feb01c1c560ba60f949e95
Source9:	http://www.pycage.de/download/skins/gdeskcal/tnf.tar.gz
# Source9-md5:	6228c6bf3e74b7fd5781aa7399bbdce9
Source10:	http://www.pycage.de/download/skins/gdeskcal/miderat_v2.tar.gz
# Source10-md5:	b135f751884f6597020f28c17c95bd9b
Source11:	http://www.pycage.de/download/skins/gdeskcal/redskin.tar.gz
# Source11-md5:	b1e4ea246a8488aa65c0a0577465973b
Source12:	http://www.pycage.de/download/skins/gdeskcal/tiny_and_simple.tar.gz
# Source12-md5:	54bdb431f47fe421ecae8b04a4c1b9d0
Source13:	http://www.pycage.de/download/skins/gdeskcal/LCD.tar.gz
# Source13-md5:	17025cacdd5b6fab611e28af7078c6fa
Source14:	http://www.pycage.de/download/skins/gdeskcal/miderat.tar.gz
# Source14-md5:	3034f02a06bd855ad20ae14fb2249993
Source15:	http://www.pycage.de/download/skins/gdeskcal/clearlemon.tar.gz
# Source15-md5:	10b38c844dbe836daac5ebeb4da7fdf1
Source16:	http://www.pycage.de/download/skins/gdeskcal/august_big.tar.gz
# Source16-md5:	28420823650d1c5b80af006d706ec48a
Source17:	http://www.pycage.de/download/skins/gdeskcal/XFCE.tar.gz
# Source17-md5:	62abdfc732a3c6aff1ab1361f50bdbac
URL:		http://www.pycage.de/software_gdeskcal_skins.html
Requires:	gDeskCal
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_skindir	%{_datadir}/gdeskcal/skins

%description
Skins for gDeskCal.

%description -l pl.UTF-8
Skórki dla gDeskCal.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_skindir}

gzip -dc %{SOURCE0} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE1} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE2} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE3} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE4} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE5} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE6} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE7} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE8} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE9} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE10} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
mv $RPM_BUILD_ROOT%{_skindir}/miderat $RPM_BUILD_ROOT%{_skindir}/miderat_v2
gzip -dc %{SOURCE11} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE12} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE13} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE14} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
mv $RPM_BUILD_ROOT%{_skindir}/miderat $RPM_BUILD_ROOT%{_skindir}/miderat_cool
gzip -dc %{SOURCE15} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE16} | tar -x -C $RPM_BUILD_ROOT%{_skindir}
gzip -dc %{SOURCE17} | tar -x -C $RPM_BUILD_ROOT%{_skindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_skindir}/*
