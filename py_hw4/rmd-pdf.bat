@echo off
set _SCRIPT_PATH=%~dp0

set var=%1

if exist %var%.pdf (if exist %var%.bak.pdf (del %var%.bak.pdf)
ren %var%.pdf %var%.bak.pdf)

if exist %var:~0,-4%.pdf (if exist %var:~0,-4%.bak.pdf (del %var:~0,-4%.bak.pdf)
ren %var:~0,-4%.pdf %var:~0,-4%.bak.pdf)

Rscript %_SCRIPT_PATH%rmd-pdf.R %1

if exist %var%.pdf (sumatra.bat %var%.pdf) else (sumatra.bat %var:~0,-4%.pdf)
