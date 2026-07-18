%global tl_name tex4ht
%global tl_revision 79674

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Convert (La)TeX to HTML/XML
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/TeX4ht
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ht.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tex4ht.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A converter from TeX and LaTeX to SGML-based formats such as (X)HTML,
MathML, OpenDocument, and Docbook, providing a configurable (La)TeX-
based authoring system for hypertext. TeX4ht does not independently
parse (La)TeX source (so it avoids the difficulties encountered by many
other converters, arising from the irregularity of (La)TeX syntax).
Instead, TeX4ht uses (La)TeX itself (with myriad macro modifications) to
produce a helper DVI file that it can then process. This technique
allows TeX4ht to approach the robustness characteristic of restricted-
syntax systems such as gellmu. Full releases of TeX4ht are no longer
made, both because it is technically difficult to do so and because
their utility is questionable. Nevertheless, TeX4ht is actively
maintained. So, current source files are held on CTAN, and updated from
the development repository frequently. Creating the myriad derived files
from them is nontrivial, and generally done with the Makefile in
development, from which the TeX4ht package in TeX Live is updated.

