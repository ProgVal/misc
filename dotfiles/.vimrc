set mouse=a
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab ts=4 sw=4 ai
set softtabstop=4
filetype plugin on
filetype plugin indent on
syntax on
set hlsearch
set nocompatible

" Return to last edit position when opening files
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

map <M-Left> gT
map <M-Right> gt

" Fix coloring for LaTeX
"autocmd BufEnter *.tex :syntax sync fromstart


""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" VimOrganizer
let g:ft_ignore_pat = '\.org'
au! BufRead,BufWrite,BufWritePost,BufNewFile *.org 
au BufEnter *.org            call org#SetOrgFileType()
command! OrgCapture :call org#CaptureBuffer()
command! OrgCaptureFile :call org#OpenCaptureFile()

let g:org_todo_setup='TODO STARTED | DONE CANCELED'
let g:org_agenda_select_dirs=["~/org_files"]
let g:org_agenda_files = split(glob("~/org_files/*.org"),"\n")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Coq
command Coq CoqIDESetMap

autocmd BufRead,BufNewFile /home/progval/ens/stageM1/* :setlocal ts=2 sw=2 tabstop=2 shiftwidth=2 softtabstop=2
autocmd BufRead,BufNewFile /home/progval/ens/stageM1/otawa/* :setlocal ts=8 sw=8 tabstop=8 shiftwidth=8 softtabstop=8
autocmd BufRead,BufNewFile /home/progval/ens/stageM1/*.py :setlocal ts=4 sw=4 tabstop=4 shiftwidth=4 softtabstop=4

""""""""""""""""""""""""""""""""""""""""""""""""""""""
" vim-latexsuite
set grepprg=grep\ -nH\ $*
let g:tex_flavor='latex'
let Tex_FoldedSections=""
let Tex_FoldedEnvironments=""
let Tex_FoldedMisc=""
" Don't disable é
" http://vim-latex.sourceforge.net/index.php?subject=faq&title=FAQ#faq-e-acute
imap <buffer> <leader>it <Plug>Tex_InsertItemOnThisLine
