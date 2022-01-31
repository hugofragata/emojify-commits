# emojify-commits
Every 🖐️ commit message 💬 deserves automatic emojis 🎉

## ⁉️ What is this?

This is basically a git hook, a prepare-commit-msg one, written in Python.
This script runs everytime you add a commit.
It grabs your commit message, parses through it and... adds emojis!
If the message contains words present in tags or description of the emoji (see emoji.json) that emoji is added to the message.
If the script is unable to find a matching emoji it chooses two random emojis, because why not.

## 🤔 How do I make my commits full of emojis?

Since it is a git hook you have to add it to a specific repo. Make sure you have Python 3+.
Open a terminal, change directory to your local repository, and run this command:

```sh
wget https://raw.githubusercontent.com/hugofragata/emojify-commits/master/install.sh -O - | sh
```

Then just commit like you'd do usually, the emojis shall appear magically 🔮, like this.
![usage](https://i.imgur.com/WfV1G09.png "Usage")


##### [License](https://github.com/me-shaon/GLWTPL)
