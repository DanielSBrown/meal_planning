# Meal Planning
## Web app that scrapes and stores recipes from meal box delivery companies
## Tech Stack

* Python + Django
* Versions (as of 10/11/22):
  * Python version: 3.11.0
  * Django version: 4.1.3
  * Postgres version: 14.1
* Built with Docker and docker compose
* Scripts executable in the bin directory along with `just`
* CI built for Github and Github Actions
  * Reference file: `.github/workflows/ci.yml`

## Technical Environments

### TODO: Add more details about the environments when they're up

## Local Development

### System Dependencies
1. [Docker](https://www.docker.com)
2. [just](https://github.com/casey/just)
### Get the code

1. Clone the repo
   ```
   git clone git@github.com:vigetlabs/meal_planning.git
   ```

### Set up pre-commit and hooks

1. Run the setup script to install pre-commit and set up the git hooks
   ```
   bin/setup
   ```
1. At any time, you can manually execute the hooks like this:
   ```
   bin/lint
   ```
1. If you want to skip the hooks, you can use the `--no-verify` flag
   ```
   git commit --no-verify
   ```
1. Run the project-specific commands (as needed)
   ```
   just makemigrations
   just reset
   # etc.
   ```
### Configure environment variables

1. If the setup script did not correctly create an `.env` file, create one:
   ```
   cp .env.example .env
   ```
1. Replace the variables in your `.env` file with the ones you got in the steps above.

### Rebuild containers if necessary

If dependencies have changed, rebuild the containers with:
```
just rebuild
```
This should fix errors like, "No module named 'Some newly added package.'"


### Tests and Coverage

1. To run the tests without coverage:
   ```
   bin/test
   ```
1. To run a single test file, just pass in the path, for example:
   ```
   bin/test apps/core/tests/test_admin.py
   ```
1. If you want to run the tests and open the coverage report in your browser, run:
   ```
   bin/cov
   ```


### Run the application

```
bin/server
```
1. You can now access the app at `localhost:8000`

### Set up data

We need to create a superuser in order to access the admin.

```
just createsuperuser
```
1. Use the CLI from above to create your user
1. Go to `localhost:8000/admin`
1. Log in using that user to access the admin

### bin executables

This project contains some standard executables in the `bin` directory. These are intended to be used in the development environment. They are not intended to be used in production.

1. `bin/bootstrap` will install the python version and pip.
1. `bin/setup` will run the bootstrap script, create the `.env` file from `.env.example`, and set up the git hooks.
1. `bin/update` will rerun the boostrap script. Used mostly by other scripts, you will rarely run this.
1. `bin/server` will run the server.
1. `bin/lint` will lint all of the files using pre-commit.
1. `bin/test` will run the pytest test suite.
1. `bin/cov` will run the pytest test suite with coverage enabled and open the coverage file.
1. `bin/ci` will be used in CI to run the test suite, check for coverage, and fail if below 100%.

### 'just' commands

To make development a little easier, some common commands are set up as executables. The current available options are below. To view the commands in your terminal, run `just -l`.

1. `just shell` will open a shell_plus instance in your terminal.
1. `just makemigrations` will call the django makemigrations command, creating migrations file from changes to models.
1. `just migrate` will call unapplied migrations.
1. `just reset` will reset the database and rerun migrations.
1. `just rebuild` will rebuild the docker containers.
1. `just createsuperuser` will open a CLI for creating a django superuser.
1. `just bash` will open a bash shell into the docker container itself.


## Adding Python Dependencies
Since this project is run and built through Docker, there is a certain workflow for adding a dependency.
- Open the particular requirement file
  - `base.txt`, `local.txt`, `production.txt` depending on what your package does
    - For a package that will be used in all environments, add to `base.txt`. For things just used locally (debugging, testing), add to `local.txt`. For production-only add to `production.txt`
- Add the package name where it makes sense in the file
  - i.e. add a new line with

      ```
      pytest-django==4.0.4
      ```

  in the section of other django or pytest packages
- Close any running backend containers
- Rebuild the backend container
  - This can be done in its own step
      ```
      just rebuild
      ```
- OPTIONAL: Bash into the container
   ```
   just bash
   ```
- and check that the package is installed
   ```
   pip list --format=freeze
   ```
   if you did not provide a package version, you should see the version number in the output. Please put this version number in the requirements file.
