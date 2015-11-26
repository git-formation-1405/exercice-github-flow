# Exercise to practice collaborative GitHub workflow

This is an exercises that we will run in groups and we number the groups
1, 2, ..., etc.

First fork this repository and then clone the fork.

Then add a file `groupN.py` where N is your group number, e.g. `group17.py`.

This file should contain a function called `tweet()` which returns
a string of maximum 140 characters, for instance:
```
def tweet():
    return "please replace this boring sentence with something more fun"
```

The file `main.py` automatically calls all `tweet()` functions defined in files
`groupN.py` (1 <= N <= 50). You do not need to edit `main.py`.

You can test it:
```
$ python main.py

group 17 says: please replace this boring sentence with something more fun
```

Once you see your sentence correctly printed, commit and push.
Then file a pull request towards the repository where you forked from.

Wait until we integrate all pull requests into the central repo
together.

Once this is done, practice to update your forked repo with
the upstream changes and verify that you got the files
created by other groups:
```
$ python main.py
```
