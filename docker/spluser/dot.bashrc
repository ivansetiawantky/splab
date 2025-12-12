#
# Additional .bashrc setting, just for interactive session inside container.
umask 022

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth:erasedups

# Ignore some controlling instructions
HISTIGNORE="[   ]*:&:bg:fg:exit:ex:history"

# Whenever displaying the prompt, write the previous line to disk
PROMPT_COMMAND="history -a"

# Don't wait for job termination notification
set -o notify

# Don't use ^D to exit
set -o ignoreeof

# Do not overwrite with >
set -o noclobber

# Use case-insensitive filename globbing
shopt -s nocaseglob

# When changing directory small typos can be ignored by bash
# for example, cd /vr/lgo/apaache would find /var/log/apache
shopt -s cdspell
shopt -s dirspell direxpand

bind "set completion-ignore-case on"
bind 'set show-all-if-ambiguous on'
#bind 'TAB:menu-complete'

# Some example alias instructions
# If these are enabled they will be used instead of any instructions
# they may mask.  For example, alias rm='rm -i' will mask the rm
# application.  To override the alias instruction use a \ before, ie
# \rm will call the real rm not the alias.

# Interactive operation...
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Default to human readable figures
alias df='df -h'
alias du='du -h'

alias pu='pushd'
alias po='popd'
alias rmtilde='/bin/rm -f *~'
alias ex='exit'
alias treeacl='tree -A -C -L 2'
alias treecl='tree -C -L 2'

#PAGER=less
export EDITOR="vi"
export LESS="-X -R"

# Enable Control-s for isearch command in bash prompt. Reverse of C-r.
[[ $- == *i* ]] && stty -ixon

# Below to manipulate directory stack with "d" command.
alias dirsv='dirs -v'
alias d='dirs -v'

# pushd with duplication ignore.
# https://unix.stackexchange.com/questions/288492/removing-duplicates-from-pushd-popd-paths
dedup(){
    declare -a new=() copy=("${DIRSTACK[@]:1}")
    declare -A seen
    local v i
    seen["$PWD"]=1
    for v in "${copy[@]}"
    do if [ -z "${seen["$v"]}" ]
       then new+=("$v")
            seen["$v"]=1
       fi
    done
    dirs -c
    for ((i=${#new[@]}-1; i>=0; i--))
    do      builtin pushd -n "${new[i]}" >/dev/null
    done
}

pushd(){
    builtin pushd "$@" > /dev/null
    dedup
    dirs
}

# replace cd with pushd https://gist.github.com/mbadran/130469
# The pushd is NOT the builtin pushd, but the pushd with duplication ignore.
function push_cd() {
  # typing just `push_cd` will take you $HOME ;)
  if [ -z "$1" ]; then
    push_cd "$HOME"

  # use `push_cd -` to visit previous directory
  elif [ "$1" == "-" ]; then
    if [ "$(dirs -p | wc -l)" -gt 1 ]; then
      current_dir="$PWD"
      popd > /dev/null
      pushd -n $current_dir > /dev/null
    elif [ -n "$OLDPWD" ]; then
      push_cd $OLDPWD
    fi

  # use `push_cd -g N` to go to the Nth directory in history (pushing)
  elif [ "$1" == "-g" ] && [[ $2 =~ ^[0-9]+$ ]]; then
    indexed_path=$(dirs -p | sed -n $(($2+1))p)
    push_cd "$(eval echo "$indexed_path")"
    #eval push_cd "$indexed_path"  # NG if dir name have space.

  # use `push_cd +N` to go to the Nth directory in history (pushing)
  elif [[ $1 =~ ^\+[0-9]+$ ]]; then
    push_cd -g ${1/+/}

  # use `push_cd -- <path>` if your path begins with a dash
  elif [ "$1" == "--" ]; then
    shift
    pushd -- "$@" > /dev/null

  # basic case: move to a dir and add it to history
  else
    pushd "$@" > /dev/null
  fi
}

# replace standard `cd` with enhanced version, ensure tab-completion works
# TO use builtin cd: unalias cd OR execute \cd OR builtin cd
alias cd=push_cd
complete -d cd

for i in $(seq 1 9); do alias "$i"="cd +${i}"; done

# git prompt
export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWUNTRACKEDFILES=true
source /home/spluser/.git-prompt.sh
source /home/spluser/.svn-prompt.sh

last_exec_status() { local e=$?; [ $e != 0 ] && echo -e "$e "; }

PS1='${debian_chroot:+($debian_chroot)}\[\e[38;5;202m\]$(last_exec_status)\[\033[34m\]\D{%m/%d %H:%M:%S }\[\e[38;5;245m\]\u\[\e[00m\]@\[\e[38;5;172m\]\h\[\033[00m\](\j):\[\e[38;5;5m\]\w\[\033[0;31m\]$(__git_ps1 "(%s)")$(__svn_prompt)\[\033[00m\]
\$ '

# Automatically activate python venv in terminal inside container:
if [[ -f /home/spluser/venv/bin/activate ]] ; then
    source /home/spluser/venv/bin/activate
fi
