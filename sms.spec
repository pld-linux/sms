Summary:	Send SMS via Polish GSM operators
Summary(pl):	Program do wysy³ania krótkich wiadomo¶ci (SMS)
Name:		sms
Version:	2.0.0
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
# Source0-md5:	6651efecd15f93e78b08f225e77b3e60
Source1:	smsq
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	curl-devel
BuildRequires:	pcre-devel
BuildRequires:	pcre++-devel
BuildRequires:	rpm-build >= 4.0.2-48
Obsoletes:	sms-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to mobile phones operaterd by Polish GSM
operators: Era, Plus and Idea.

%description -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup -q -n %{name}-%{version}

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
%doc README* doc/*
%doc contrib/{mimecut,procmailrc,sms-get}
%attr(755,root,root) %{_bindir}/sms
%attr(755,root,root) %{_bindir}/smsaddr
%attr(755,root,root) %{_bindir}/smsq
