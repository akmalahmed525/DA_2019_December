# Crime Data Analysis of the City of Chicago (USA) from the year 2001 to Present date

>The data is extracted from the [CLEAR](https://data.cityofchicago.org/Public-Safety/Crimes-2019/w98m-zvie) (Citizen Law Enforcement Analysis and Reporting) system.
>Note: We limit the data objects to 10000, according to our instruction.

1. Clone the repository.
2. Create a folder `data` via the command below.

```bash
    mkdir data auth
```

3. Create a `venv`.

```bash
    python3 -m venv env
```

4. Activate the `venv` via the command below.

```bash
    source env/bin/activate
```

5. We can install the packages as usual.

6. After development freeze the local python environment.

```bash
    pip3 freeze --local > requirements.txt
```

7. Install the packages via the command below.

```bash
    pip3 install -r requirements.txt
```

> for authentication

```bash
    export GOOGLE_APPLICATION_CREDENTIALS="$PWD/auth/YOUR_AUTH_CREDENTIALS.json"
```
