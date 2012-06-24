
#NOTE:	latest working ver of curl with ideambox is 7.12.1
#	tested on 7.12.1-7.14.0

Summary:	Send SMS via Polish GSM operators
Summary(pl):	Program do wysy�ania kr�tkich wiadomo�ci (SMS)
Name:		sms
Version:	2.0.3
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
# Source0-md5:	d238c15e705aa4999aaf459e2fc1e821
Source1:	smsq
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	curl-devel
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pcre-devel
BuildRequires:	pcre++-devel
BuildRequires:	rpm-build >= 4.0.2-48
Obsoletes:	sms-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to mobile phones operaterd by Polish GSM
operators: Era, Plus and Idea.

%description -l pl
Program potrafi wysy�a� wiadomo�ci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sms $RPM_BUILD_ROOT%{_bindir}
install smsaddr $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README* doc/readme.html
%doc contrib/{mimecut,procmailrc,sms-get}
%attr(755,root,root) %{_bindir}/sms
%attr(755,root,root) %{_bindir}/smsaddr
%attr(755,root,root) %{_bindir}/smsq
