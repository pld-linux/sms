Summary:	Program send SMS
Summary(pl):	Program do wysy³ania SMS
Name:		sms
Version:	1.8.9i
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
Patch0:		%{name}-c++.patch
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to phone Era, Plus and Idea.

%description -l pl
Program potrafi wysy³aæ wiadomo¶ci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup  -q -n %{name}
%patch0 -p1

%build
%{__make} CC="%{__cc}" CXX="%{__cxx}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sms smsaddr $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README* contrib/{gtksms,mimecut,procmailrc,sms-conf,sms.cgi,sms.html} \
		contrib/tksms/* doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* contrib doc
%attr(755,root,root) %{_bindir}/*
