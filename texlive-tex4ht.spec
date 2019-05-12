Name:		texlive-tex4ht
Version:	20190409
Release:	2
Summary:	Convert (La)TeX to HTML/XML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/support/TeX4ht
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.doc.tar.xz
# The so-called source in CTAN includes a prebuilt Java jar file... Let's overwrite
# that with one built from the real source, available at
# svn checkout http://svn.gnu.org.ua/sources/tex4ht/trunk tex4ht-source
Source2:	tex4ht-source-562.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
BuildRequires:	jmod(java.desktop)
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-tex4ht.bin
%rename tex4ht

BuildRequires:	jdk-current
BuildRequires:	javapackages-local

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
%{_javadir}/tex4ht.jar
%doc %{_texmfdistdir}/doc/generic/tex4ht

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2
. %{_sysconfdir}/profile.d/90java.sh
export PATH=$JAVA_HOME/bin:$PATH

cd tex4ht-source-562/src/java
cat >module-info.java <<'EOF'
module tex4ht {
	exports xtpipes;
	exports xtpipes.util;
	requires java.desktop;
}
EOF
find . -name "*.java" |xargs javac
find . -name "*.class" -o -name "*.properties" |xargs jar cf tex4ht.jar
pwd
cp -f tex4ht.jar ../../../texmf-dist/tex4ht/bin/

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
mkdir -p %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
    ln -sf %{_texmfdistdir}/tex4ht/bin/tex4ht.jar tex4ht.jar
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
