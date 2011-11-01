Name:		texlive-decorule
Version:	0.6
Release:	1
Summary:	Decorative swelled rule using font character
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/decorule
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package implements a decorative swelled rule using only a
symbol from a font installed with all distributions of TeX, so
it works independently, without the need to install any
additional software or fonts. This is the packaged version of
the macro which was originally published in the "Typographers'
Inn" column in TUGboat 31:1 (2010).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/decorule/decorule.sty
%doc %{_texmfdistdir}/doc/latex/decorule/MANIFEST
%doc %{_texmfdistdir}/doc/latex/decorule/README
%doc %{_texmfdistdir}/doc/latex/decorule/decorule.pdf
#- source
%doc %{_texmfdistdir}/source/latex/decorule/decorule.dtx
%doc %{_texmfdistdir}/source/latex/decorule/decorule.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
