Summary:	Program send SMS
Summary(pl):	Program do wysy³ania SMS
Name:		sms
Version:	1.8.9i
Release:	5
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-c++.patch
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.0.2-48
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to phone Era, Plus and Idea.

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
This program sends SMS to phone Era, Plus and Idea.
This package allows to use simple Tk X11 interface.

%description X11 -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea. Ten pakiet dostarcza prosty interfejs w Tk dla X11.

%prep
%setup  -q -n %{name}
%patch0 -p1

%build
%{__make} CC="%{__cc}" CXX="%{__cxx}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},/usr/X11R6/bin,%{_applnkdir}/Network/Misc}

install sms smsaddr $RPM_BUILD_ROOT%{_bindir}
install contrib/tksms/tksms $RPM_BUILD_ROOT/usr/X11R6/bin/
install contrib/tksms/sms_wr $RPM_BUILD_ROOT/usr/X11R6/bin/
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc/sms-Tk.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
gzip -9nf README* contrib/{gtksms,mimecut,procmailrc,sms-conf,sms.cgi,sms.html} \
		contrib/tksms/README doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* contrib/*.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
%{_applnkdir}/Network/Misc/*
%doc contrib/tksms/*.gz
%{_pixmapsdir}/*.png
