syntax on
set mouse=a
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab ts=4 sw=4 ai
set softtabstop=4
filetype plugin on
filetype plugin indent on
set hlsearch
set nocompatible

" Return to last edit position when opening files
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

map <M-Left> gT
map <M-Right> gt

command Coq CoqIDESetMap
