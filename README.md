
## Git Bisect Tutorial
This repository is part of a series of practical contents developed to demonstrate test techniques.

### Running this example
If you want to run this code, make a clone of this repository and follow these steps:

    $ git bisect start	// Starts git bisect
    $ git bisect bad	// This repository is broken, so we set to bad
    $ git bisect good 58ecb3e	// Our first commit was good, so let's set it to good
    $ git bisect reset  // Exits from ``git bisect`` running