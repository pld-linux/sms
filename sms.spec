Summary:	Program send SMS
Summary(pl):	Program do wysy�ania SMS
Name:		sms
Version:	1.8.9e
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
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
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sms smsaddr $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README* contrib/* doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* contrib doc
%attr(755,root,root) %{_bindir}/* 
