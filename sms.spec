Summary:	Program send SMS
Summary(pl):	Program do wysylania SMS
Name:		sms
Version:	1.8.8d
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://www.ceti.pl/~miki/komputery/download/sms/%{name}-%{version}.tar.gz
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program send SMS to phone Era, Plus and Idea.

%description -l pl
Program potrafi wysylac wiadomosci na telefony sieci Era, Plus oraz
Idea.

%prep
%setup  -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}"

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
