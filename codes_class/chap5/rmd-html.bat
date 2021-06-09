@echo off
set _SCRIPT_PATH=%~dp0

set var=%1

if exist %var%.html (
if exist %var%.bak.html (del %var%.bak.html)
ren %var%.html %var%.bak.html
)

if exist %var:~0,-4%.html (
if exist %var:~0,-4%.bak.html (del %var:~0,-4%.bak.html)
ren %var:~0,-4%.html %var:~0,-4%.bak.html
)

Rscript %_SCRIPT_PATH%rmd-html.R %1


if exist %var%.html (start %var%.html) else (start %var:~0,-4%.html)


