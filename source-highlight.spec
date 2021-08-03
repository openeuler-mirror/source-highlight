Name:		source-highlight
Version:	3.1.9
Release:	2
Summary:	Source Code Highlighter with Support for Many Languages
License:	GPLv3+
URL:		http://www.gnu.org/software/src-highlite
Source0:        https://ftp.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz.sig

BuildRequires:	bison boost-devel chrpath ctags flex gcc gcc-c++ help2man bash-completion
Requires:       ctags	

%description
This program, given a source file, produces a document with syntax highlighting.

Source-highlight reads source language specifications dynamically, thus it can
be easily extended (without recompiling the sources) for handling new languages. 
It also reads output format specifications dynamically, and thus it can be 
easily extended (without recompiling the sources) for handling new output 
formats. The syntax for these specifications is quite easy (take a look at the 
manual).

Source-highlight is a command line program, and it can also be used as a CGI.

%package        devel
Summary:        Header files for source-highlight
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for source-highlight

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --with-boost-regex=boost_regex
%make_build

%install
%make_install
%delete_la

mv $RPM_BUILD_ROOT%{_datadir}/doc/ docs
sed -i 's/\r//' docs/source-highlight/*.css

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight-settings

echo -e "\ncxx = cpp.lang" >> $RPM_BUILD_ROOT%{_datadir}/source-highlight/lang.map

bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
install -p -d $RPM_BUILD_ROOT$bashcompdir

pushd $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -p -m 755 source-highlight $RPM_BUILD_ROOT$bashcompdir/
popd

%files
%defattr(-,root,root)
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/check-regexp
%{_bindir}/*html
%{_bindir}/source-highlight*
%{_bindir}/src-hilite-lesspipe.sh
%{_libdir}/libsource-*.so*
%{_datadir}/bash-completion/completions/source-highlight
%{_datadir}/source-highlight/*
%exclude %{_sysconfdir}/bash_completion.d

%files devel
%defattr(-,root,root)
%{_includedir}/srchilite/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.a

%files help
%doc docs/source-highlight/*
%{_mandir}/man1/*.gz
%{_datadir}/info/*.info.gz
%exclude %{_datadir}/info/dir

%changelog
* Mon Aug 02 2021 chenyanpanHW <chenyanpan@huawei.com> - 3.1.9-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Thu Jan 28 2021 jinzhimin <jinzhimin2@huawei.com> - 3.1.9-1
- upgrate to 3.1.9

* Wed Dec 16 2020 zhanzhimin <zhanzhimin@huawei.com> - 3.1.8-24
- Update Source0

* Wed Jan 22 2020 openEuler Buildteam <buildteam@openeuler.org> - 3.1.8-23
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add git in buildrequires

* Thu Oct 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1.8-22
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add license files to rpm package

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1.8-21
- Package init
