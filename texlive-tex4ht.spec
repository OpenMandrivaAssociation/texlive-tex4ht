Name:		texlive-tex4ht
Version:	71381
Release:	1
Summary:	Convert (La)TeX to HTML/XML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/support/TeX4ht
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.source.r%{version}.tar.xz
# Additional sources available at
# svn checkout http://svn.gnu.org.ua/sources/tex4ht/trunk tex4ht-source
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
BuildRequires:	jmod(java.desktop)
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-tex4ht.bin
%rename tex4ht

BuildRequires:	jdk-current

%description
A converter from TeX and LaTeX to SGML-based formats such as
(X)HTML, MathML, OpenDocument, and DocBook, providing a
configurable (La)TeX-based authoring system for hypertext.
Tex4ht does not parse (La)TeX source (so that it avoids the
difficulties encountered by many other converters, arising from
the irregularity of (La)TeX syntax). Instead, Tex4ht uses
(La)TeX itself (with an extra macro package) to produce a non-
standard DVI file that it can then process. This technique
allows TeX4ht to approach the robustness characteristic of
restricted-syntax systems such as hyperlatex and gellmu. Note
that CTAN no longer holds the definitive sources of the
package: see the 'Readme' file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_texmfdistdir}/scripts/tex4ht
%{_texmfdistdir}/tex/generic/tex4ht
%{_texmfdistdir}/tex4ht
%{_datadir}/java/tex4ht.jar
%doc %{_texmfdistdir}/doc/generic/tex4ht
%doc %{_texmfdistdir}/source/generic/tex4ht

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/tex4ht/ht.sh ht
ln -sf %{_texmfdistdir}/scripts/tex4ht/htcontext.sh htcontext
ln -sf %{_texmfdistdir}/scripts/tex4ht/htlatex.sh htlatex
ln -sf %{_texmfdistdir}/scripts/tex4ht/htmex.sh htmex
ln -sf %{_texmfdistdir}/scripts/tex4ht/httex.sh httex
ln -sf %{_texmfdistdir}/scripts/tex4ht/httexi.sh httexi
ln -sf %{_texmfdistdir}/scripts/tex4ht/htxelatex.sh htxelatex
ln -sf %{_texmfdistdir}/scripts/tex4ht/htxetex.sh htxetex
ln -sf %{_texmfdistdir}/scripts/tex4ht/mk4ht.pl mk4ht
popd
mkdir -p %{buildroot}%{_datadir}/java
pushd %{buildroot}%{_datadir}/java
ln -sf %{_texmfdistdir}/tex4ht/bin/tex4ht.jar tex4ht.jar
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
