---
title: {{title}}
documentclass: report
geometry: margin=1in
links-as-notes: true
subparagraph: true
fontsize: 12pt
mainfont: Roboto-Regular.ttf
mainfontoptions:
- Path={{fonts_dir}}/roboto-hinted/
- BoldFont=Roboto-Bold.ttf
- ItalicFont=Roboto-Italic.ttf
- BoldItalicFont=Roboto-BoldItalic.ttf
monofont: liquid-bigspace.ttf
monofontoptions:
- Path={{fonts_dir}}/liquid/
- BoldFont=liquid-bigspace.ttf
- ItalicFont=liquid-bigspace.ttf
- BoldItalicFont=liquid-bigspace.ttf
header-includes:
- \usepackage{titlesec}
- \titleformat{\chapter}{\normalfont\LARGE\bfseries}{\thechapter.}{1em}{}
- \titlespacing*{\chapter}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
- \usepackage{etoolbox}
- \AtBeginEnvironment{longtable}{\small}{}{}
- \renewcommand\arraystretch{1.3}
- \usepackage{needspace}
- \titleformat{\section}{\needspace{0.5\textheight}\normalfont\large\bfseries}{\thesection}{1em}{}
---
