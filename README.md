# emojify-commits
Every 🖐️ commit message 💬 deserves automatic emojis 🎉

## What is this?

This is basically a git hook, a prepare-commit-msg one, written in Python.
This script, specific to your repo, is run everytime you add a commit.
It grabs your commit message, parses through it and adds emojis!
If your message contains words present in tags or description of the emoji it appends that emoji.
If it unable to find a matching emoji the script adds two random emojis at the end, because why not.

## How do I make my commits full of emojis?

Since it is a git hook you have to add it to a specific repo.
Open a terminal in your local repository and run these commands:

**change to curl***
```(bash)
cp emoji.json ./.git/hooks/
cp emojify.py ./.git/hooks/prepare-commit-msg
chmod +x ./.git/hooks/prepare-commit-msg

```

Then just commit like you'd do usually, the emojis shall appear magically, like this.


------

Thanks to Gem (where I found the emoji.json)

