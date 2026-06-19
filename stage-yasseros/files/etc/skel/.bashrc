# YasserOS default .bashrc

# Source global definitions
[ -f /etc/bashrc ] && . /etc/bashrc

# Source Debian/Raspbian defaults
[ -f /etc/bash.bashrc ] && . /etc/bash.bashrc

# YasserOS branded prompt: user@hostname:dir$
# Colors: YasserBlue for user@host, Violet for dir
PS1='\[\e[38;2;68;147;248m\]\u@\h\[\e[0m\]:\[\e[38;2;163;113;247m\]\w\[\e[0m\]\$ '

# Convenience aliases
alias ll='ls -lah --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias grep='grep --color=auto'

# YasserOS shortcuts
alias ycc='yasser-control-center'
alias yos-update='sudo apt update && sudo apt upgrade -y'

# Better history
HISTSIZE=5000
HISTFILESIZE=10000
HISTCONTROL=ignoredups:erasedups
shopt -s histappend

# Announce YasserOS on login
if [ -f /etc/yasseros-release ]; then
    cat /etc/yasseros-release
fi
