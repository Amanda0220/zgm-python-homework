@echo off
set _SCRIPT_PATH=%~dp0

set var=%1

if exist %var%.docx (
if exist %var%.bak.docx (del %var%.bak.docx)
ren %var%.docx %var%.bak.docx
)

if exist %var:~0,-4%.docx (
if exist %var:~0,-4%.bak.docx (del %var:~0,-4%.bak.docx)
ren %var:~0,-4%.docx %var:~0,-4%.bak.docx
)

Rscript %_SCRIPT_PATH%rmd-doc.R %1

if exist %var%.docx (start %var%.docx) else (start %var:~0,-4%.docx)
