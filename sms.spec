Summary:	Send SMs via Polish GSM operators
Summary(pl):	Program do wysy³ania krótkich wiadomo¶ci (SMs)
Name:		sms
Version:	1.9.2g
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
# Source0-md5:	864c64792979d73d5a27681350bb4251
Patch0:		%{name}-gcc33.patch
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	smsq
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.0.2-48
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMs to mobile phones operaterd by Polish GSM operators:
Era, Plus and Idea.

%description -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea.

%package X11
Summary:	Send SMs via Polish GSM operators - Tk interface
Summary(pl):	Program do wysy³ania krótkich wiadomo¶ci (SMs) - interfejs w Tk
Group:		Networking/Utilities
Requires:	sms = %{version}
Requires:	perl-Tk

%description X11
This program sends SMS to mobile phones operated by Polish GSM operators
Era, Plus and Idea networks. This package allows to use simple Tk X11
interface.

%description X11 -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea. Ten pakiet dostarcza prosty interfejs w Tk dla X11.

%prep
%setup -q -n %{name}
#%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install {sms{,addr},contrib/tksms/{tksms,sms_wr}} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/sms-Tk.desktop
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
%attr(755,root,root) %{_bindir}/sms_wr
%attr(755,root,root) %{_bindir}/tksms
%doc contrib/tksms/README
%{_desktopdir}/sms-Tk.desktop
%{_pixmapsdir}/*.png
