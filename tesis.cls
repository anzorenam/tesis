\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tesis}[03/03/2021]
\LoadClass{book}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{mathpazo}
\RequirePackage[euler-digits,euler-hat-accent]{eulervm}
\RequirePackage[english,spanish,es-nodecimaldot]{babel}
\RequirePackage{subcaption}
\RequirePackage[intlimits]{amsmath}
\RequirePackage{amsfonts,amssymb}
\RequirePackage[inline]{enumitem}
\RequirePackage[version=4]{mhchem}
\RequirePackage{mathtools}
\RequirePackage{datetime}
\RequirePackage[separate-uncertainty=true,multi-part-units=single,binary-units]{siunitx}
\RequirePackage{booktabs}
\RequirePackage{xfrac}
\RequirePackage[hypcap]{caption}
\RequirePackage[vlined,spanish,onelanguage]{algorithm2e}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage[toc,page]{appendix}
\RequirePackage{fancyhdr}
\RequirePackage{listings}
\RequirePackage{titlesec}
\RequirePackage{fix-cm}

\RequirePackage[
			letterpaper,
			asymmetric,
			headheight=15pt,
			heightrounded,
				]{geometry}

\definecolor{light-gray}{gray}{0.7}
\definecolor{oro}{RGB}{216,112,1}
\definecolor{azul}{RGB}{12,28,71}

\RequirePackage[plainpages=false,
            bookmarksopen=true,
            bookmarksnumbered=true,
            breaklinks=true,
            linktocpage=false,
            pagebackref=true,
            pdftitle={Desarrollo de un instrumento para la detección de neutrones solares en la cima
						del Volcán Sierra Negra},
            pdfauthor={Marcos Alfonso Anzorena Méndez},
            pdfsubject={Tesis de doctorado},
            colorlinks=true,
            linkcolor=oro,
            urlcolor =azul,
            citecolor=oro,
            anchorcolor=green
            ]{hyperref}

%\renewcommand{\cleardoublepage}{\clearpage}

\linespread{1.05}
\setlength{\parindent}{0pt}
\addtolength{\parskip}{10pt}

\pagestyle{fancy}
\renewcommand\headrule{{\color{light-gray} \hrule height  2pt width \headwidth}}
\renewcommand{\headrulewidth}{2pt}
\renewcommand{\footnoterule}{}

\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}{}}

\fancyhead{}
\fancyhead[RE]{\textit{\rightmark}}
\fancyhead[LO]{\textbf{\leftmark}}
\fancyfoot[C]{\thepage}

\titleformat{\chapter}[display]
   {\Huge\bfseries}{\chaptertitlename\ \thechapter}{0pt}{\Huge}

\DeclareMathSizes{12}{20}{14}{10}

\renewcommand{\appendixname}{Apéndice}
\renewcommand{\appendixtocname}{Apéndice}
\renewcommand{\appendixpagename}{Apéndice}

\makeatletter
\@openrightfalse
\let\oriAlph\Alph
\let\orialph\alph
\renewcommand{\@resets@pp}{\par
  \@ppsavesec
  \stepcounter{@pps}
  \setcounter{section}{0}%
  \if@chapter@pp
    \setcounter{chapter}{0}%
    \renewcommand\@chapapp{\appendixname}%
    \renewcommand\thechapter{\@Alph\c@chapter}%
  \else
    \setcounter{subsection}{0}%
    \renewcommand\thesection{\@Alph\c@section}%
  \fi
  \if@pphyper
    \if@chapter@pp
      \renewcommand{\theHchapter}{\theH@pps.\oriAlph{chapter}}%
    \else
      \renewcommand{\theHsection}{\theH@pps.\oriAlph{section}}%
    \fi
    \def\Hy@chapapp{appendix}%
  \fi
  \restoreapp
}
\makeatother
