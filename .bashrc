# 1. Alias: clear the screen and show current directory
alias la='ls -a'

# 2. Shell function: make a backup copy of a file
backup ()
{
    cp "$1" "$1.bak"
}

# 3. Shell function with if-statement: go to a directory if it exists, otherwise create it first
cdd ()
{
    if [ -d "$1" ]; then
        cd "$1"
    else
        mkdir -p "$1" && cd "$1"
    fi
}
