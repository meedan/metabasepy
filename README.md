# metabasepy

## Summary

A simple class that wraps the [metabase](https://github.com/metabase/metabase) internal API. 
Easily access data from your Metabase questions for analysis in Python.

There is a similar library for R: [metabaser](https://github.com/meedan/metabaser)

This has been tested with metabase version 0.38.3 (latest avilable as of April 2021) and Python 3.

## Installation
1. Ensure the necessary packages are installed
```
pip install requests
```
2. Install this library
```
git clone https://github.com/meedan/metabasepy.git
cd metabasepy
python setup.py
```

## First example
1. Load the package
```
import metabasepy
```
2. Establish a metabase session.
```
mb=metabasepy.metabasepy("https://url/to/metabase","username","password")
```

3. Execute a query. Here is a simple question without any parameters. 
The "id" of the question is clearly visible in the querystring when using metabase in your browser.
```
result=mb.fetch_question(42)
print(result) #This is JSON
```

If you have parameters to your question, these should be added in the ``parameters`` argument as a dictionary
```
result2=mb.fetch_question(48,{"myparameter":"value","start_date":"2021-04-05"})
print(result2)
```

## Contact

Further information is available from Scott Hale. Meedan team members can 
contact Scott via Slack and others can reach out to Scott via comments/issues
on this repository or via [direct message on Twitter](https://twitter.com/computermacgyve)
