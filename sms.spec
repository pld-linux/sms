Summary:	Program send SMS
Summary(pl):	Program do wysy³ania SMS
Name:		sms
Version:	1.9.1h
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	smsq
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.0.2-48
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to Era, Plus and Idea networks.

%description -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea.

%package X11
Summary:	Program send SMS - Tk interface
Summary(pl):	Program do wysy³ania SMS - interfejs w Tk
Group:		Networking/Utilities
Requires:	sms = %{version}
Requires:	perl-Tk

%description X11
This program sends SMS to Era, Plus and Idea networks. This package
allows to use simple Tk X11 interface.

%description X11 -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea. Ten pakiet dostarcza prosty interfejs w Tk dla X11.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},/usr/X11R6/bin,%{_applnkdir}/Network/Misc}

install sms smsaddr $RPM_BUILD_ROOT%{_bindir}
install contrib/tksms/tksms $RPM_BUILD_ROOT/usr/X11R6/bin/
install contrib/tksms/sms_wr $RPM_BUILD_ROOT/usr/X11R6/bin/
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/sms-Tk.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* doc/*
%doc contrib/{gtksms,mimecut,procmailrc,sms-conf,sms.cgi,sms.html}
%attr(755,root,root) %{_bindir}/sms
%attr(755,root,root) %{_bindir}/smsaddr
%attr(755,root,root) %{_bindir}/smsq

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
%doc contrib/tksms/README
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*.png
