## Resources needed for the lab lectures
Thursday 1 October I will be holding the first lab lecture. Before that date, I would kindly ask the students to install the following programs and libraries.

# Programs
python (best a version in the 3.x series, eg. 3.8.5)
a text editor specialised for programming (e.g., Visual Studio Code)
Libraries
scikit learn
matplotlib
pydotplus
graphviz -- note: graphviz is not a python library and needs to be installed separatedly

# Suggestions
We suggest two ways to install the software (any other mean is accepted as long as everything works properly):

virtualenv: pro - minimal installation; only necessary packages getet installed; cons - it nees some work to install all the required packages.
Anaconda: pro - everything and the kitchen sink is included; cons - larger footprint w.r.t. the virtualenv installation.
Virtualenv
Since versione 3.3, a subset of virtualenv has been included in python. To create a new virtualenv it suffices to launch from the command line:

   python3 -m venv DIRNAME
The given command will create a new directory named DIRNAME. Everything needed to support the virtualenv will be written into the given directory. After the virtualenv is created, it can be activated by using the command:

   source DIRNAME/bin/activate.sh
(note: we are assuming that you are working on bash shell, but keep in mind that the directory bin inside DIRNAME contains scripts to support most of the shells in common use).

When the virtualenv is active, any command is executed within that context. To install a new package simply proceed as if you were not in the virtualenv. The only difference will be that the packages and their configurations will be written inside the virtualenv instead of being written on a globally available path. After that if you invoke python, the interpreter will see only the packages installed within the virtual environment (this avoids any possible conflict with python libraries installed elsewhere).

Anaconda
See https://conda.io/docs/user-guide/tasks/manage-environments.html for some explanations on how to create environments.
