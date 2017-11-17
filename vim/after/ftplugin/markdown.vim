setlocal shiftwidth=4
setlocal tabstop=4
setlocal softtabstop=4
setlocal colorcolumn=0
setlocal textwidth=0
setlocal expandtab
setlocal wrap linebreak showbreak=↪
setlocal autoindent
setlocal formatoptions=tcqn

" Mark ✓
nnoremap zmm i<c-k>OK<Space>
inoremap zmm<Tab> <c-k>OK<Space>
nnoremap zzm cl<c-k>OK<Esc>

" Mark ✗
nnoremap zxx i<c-k>XX<Space>
inoremap zxx<Tab> <c-k>XX<Space>
nnoremap zzx cl<c-k>XX<Esc>

" Mark ○
nnoremap zoo i<c-k>0m<Space>
inoremap zoo<Tab> <c-k>0m<Space>
nnoremap zzo cl<c-k>0m<Esc>

" ├─
nnoremap ztt i<c-k>vr<c-k>hh<Space>
inoremap ztt<Tab> <c-k>vr<c-k>hh<Space>
nnoremap zzt cl<c-k>vr<Esc>

" └─
nnoremap zee i<c-k>ur<c-k>hh<Space>
inoremap zee<Tab> <c-k>ur<c-k>hh<Space>
nnoremap zze cl<c-k>ur<Esc>

" │
nnoremap zvv i<c-k>vv<Space><Space>
inoremap zvv<Tab> <c-k>vv<Space><Space>
nnoremap zzv cf<c-k>hh<c-k>vv<Space><Esc>

" Underline
nnoremap zuu yypVr-k<c-v>jI<Space><Esc>

" Highlight headlines
nnoremap zhh /^#.*<CR>

" Make headline
nnoremap zzh I#<Space><Esc>
nnoremap zzh2 I##<Space><Esc>

" …
nnoremap z3. i<C-v>u2026<Esc>
inoremap z3.<Tab> <C-v>u2026
