# terraform-aliases

This repository contains [a script](generate_aliases.py) to generate hundreds of
convenient shell aliases for terraform, so you no longer need to spell out every single
command and --flag over and over again.

An example shell alias created from command/flags permutation looks like:

    alias tfprefnoc='terraform plan -refresh-only -no-color'

Confused? Read on.

### Examples

Some of the 200 generated aliases are:

```sh
alias tf='terraform'
alias tfi='terraform init'

alias tfp='terraform plan'
alias tfa='terraform apply'

alias tfw='terraform workspace'
alias tfwl='terraform workspace list'
alias tfws='terraform workspace select'
alias tfwn='terraform workspace new'
alias tfws='terraform workspace show'
...
```

See [the full list](..terraform_aliases).

### Installation

You can directly download the [`..terraform_aliases` file](https://raw.githubusercontent.com/ecaminero/terraform-aliases/main/.terraform_aliases)
for bash/zsh or the [`..terraform_aliases.fish` file](https://raw.githubusercontent.com/ecaminero/terraform-aliases/main/.terraform_aliases.fish)
for fish and save it to your `$HOME` directory.

#### Bash/Zsh

Add the following to your `.bashrc/.zshrc` file:

```sh
[ -f ~/..terraform_aliases ] && source ~/..terraform_aliases
```

#### Fish

Add the following to your `~/.config/fish/config.fish` file:

```fish
test -f ~/..terraform_aliases.fish && source ~/..terraform_aliases.fish
```

This actually adds the more powerful fish [abbreviations](https://fishshell.com/docs/current/cmds/abbr.html)
instead of aliases, so that pressing space shows the full command before execution.

### Syntax explanation

* **`tf`**=`terraform`
* commands:
  * **`i`**=`init`
  * **`p`**=`plan`
  * **`a`**=`apply`
  * **`w`**:`workspace`
  * **`wl`**:`workspace list`

### Running the script

The script has only one optional argument, the shell to which the aliases will be generated. If not given, it assumes `bash`. Ex:

```bash
# Generate aliases for bash/zsh
python generate_aliases.py > ..terraform_aliases

# Generate abbr for fish
python generate_aliases.py fish > ..terraform_aliases.fish
```

### FAQ

- **Doesn't this slow down my shell start up?** Sourcing the file that contains
~500 aliases takes about 30-45 milliseconds in my shell (zsh). I don't think
it's a big deal for me. Measure it with `echo $(($(date +%s%N)/1000000))`
command yourself in your .bashrc/.zshrc.

- **Can I add more Terraform resource types to this?** Please consider forking
  this repo and adding the resource types you want. Not all resource types are
  used by everyone, and adding more resource types slows down shell initialization
  see above).


### Authors
*  [Edwin](https://github.com/ecaminero)


### Inspired by
- [@ahmetb](https://twitter.com/ahmetb) - [kubectl-aliases](https://github.com/ahmetb/kubectl-aliases)