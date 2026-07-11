%global tl_name ucbthesis
%global tl_revision 51690

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.6
Release:	%{tl_revision}.1
Summary:	Thesis and dissertation class supporting UCB requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucbthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucbthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucbthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides the necessary framework for electronic submission of
Masters theses and Ph.D. dissertations at the University of California,
Berkeley. It is based on the memoir class.

