Name:		texlive-decorule
Version:	55230
Release:	2
Summary:	Decorative swelled rule using font character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/decorule
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decorule.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements a decorative swelled rule using only a
symbol from a font installed with all distributions of TeX, so
it works independently, without the need to install any
additional software or fonts. This is the packaged version of
the macro which was originally published in the "Typographers'
Inn" column in TUGboat 31:1 (2010).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/decorule
%doc %{_texmfdistdir}/doc/latex/decorule
#- source
%doc %{_texmfdistdir}/source/latex/decorule

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
