Summary:	Program send SMS
Summary(pl):	Program do wysylania SMS
Name:		sms
Version:	1.8.6b
Release:	1
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
Requires:	gdbm
BuildRequires:	gdbm-devel

%description
This program send SMS to phone Era, Plus and Idea.

%description -l pl
Program potrafi wysylac wiadomosci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup  -q -n sms

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d		$RPM_BUILD_ROOT%{_bindir}
install sms		$RPM_BUILD_ROOT%{_bindir}
install smsaddr		$RPM_BUILD_ROOT%{_bindir}

tar czf contrib.tar.gz contrib
tar czf doc.tar.gz doc
gzip -9nf README*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/* 
%doc README* contrib.tar.gz doc.tar.gz
