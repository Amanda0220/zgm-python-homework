@echo off
set _SCRIPT_PATH=%~dp0

set var=%1

if exist %var%_bearmer.pdf (if exist %var%_bearmer.bak.pdf (del %var%_bearmer.bak.pdf)
ren %var%_bearmer.pdf %var%_bearmer.bak.pdf)

if exist %var:~0,-4%_bearmer.pdf (if exist %var:~0,-4%_bearmer.bak.pdf (del %var:~0,-4%_bearmer.bak.pdf)
ren %var:~0,-4%_bearmer.pdf %var:~0,-4%_bearmer.bak.pdf)

Rscript %_SCRIPT_PATH%rmd-beamer.R %1

if exist %var%_beamer.pdf (sumatra.bat %var%_beamer.pdf) else (sumatra.bat %var:~0,-4%_beamer.pdf)