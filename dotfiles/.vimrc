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
autocmd BufEnter *.tex :syntax sync fromstart


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
