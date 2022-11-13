Name:		texlive-ucbthesis
Version:	51690
Release:	1
Summary:	TeXLive ucbthesis package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucbthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucbthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ucbthesis package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucbthesis/ucbthesis.cls
%doc %{_texmfdistdir}/doc/latex/ucbthesis/README
%doc %{_texmfdistdir}/doc/latex/ucbthesis/example/abstract.tex
%doc %{_texmfdistdir}/doc/latex/ucbthesis/example/chap1.tex
%doc %{_texmfdistdir}/doc/latex/ucbthesis/example/chap2.tex
%doc %{_texmfdistdir}/doc/latex/ucbthesis/example/references.bib
%doc %{_texmfdistdir}/doc/latex/ucbthesis/example/thesis.tex
%doc %{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.pdf
%doc %{_texmfdistdir}/doc/latex/ucbthesis/ucbthesis.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
