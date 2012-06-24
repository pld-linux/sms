Summary:	Program send SMS
Summary(pl):	Program do wysy�ania SMS
Name:		sms
Version:	1.8.9c
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narz�dzia
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
URL:		http://ceti.pl/~miki/komputery/sms.html
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to phone Era, Plus and Idea.

%description -l pl
Program potrafi wysy�a� wiadomo�ci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup  -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sms smsaddr $RPM_BUILD_ROOT%{_bindir}

tar czf contrib.tar.gz contrib
tar czf doc.tar.gz doc

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* contrib.tar.gz doc.tar.gz
%attr(755,root,root) %{_bindir}/* 
