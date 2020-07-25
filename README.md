## Git Bisect Tutorial

This repository is part of a series of practical contents developed to demonstrate test techniques.

### Running this example

If you want to run this code, make a clone of this repository and follow these steps:

	$ git bisect start 		// Starts git bisect
	$ git bisect bad master 	// This repository is broken, so we set to bad
	$ git bisect good 58ecb3e 	// Our first commit was good, so let's set it to good

Now you will run ``git bisect good`` if the code is running well. If it isn't working, you'll run ``git bisect bad``. Repeat these steps until it finds the buggy commit (98f2c97):

	98f2c97da730b5b7aa4bc09bd6d311eae3ebefd0 is the first bad commit
	commit 98f2c97da730b5b7aa4bc09bd6d311eae3ebefd0
	Author: Fernando Alves <fehaa2000@gmail.com>
	Date:   Sat Jul 25 15:13:15 2020 -0300

	    [BUG] Change return when number is equal to 1

	 factorial.py | 2 +-

Once it's done, you must exit from ``git bisect`` running:

	$ git bisect reset	//Exits from ``git bisect`` running
