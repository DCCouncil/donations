# About Council Donations

Pursuant to D.C. Official Code § 1-329.01, the Council may accept donations for the Council to "carry out its authorized functions or duties." For the past few years, the Council has used a combination of spreadsheets and Sharepoint-based forms to collect the data. The information was then collected and compiled in Excel, and converted to CSV and PDF formats. In Council Period 21, however, the Council will collect the data using this site and the data will publish automatically in a web-friendly format.

## API Documentation

The Council Donations site is built using Django (see the source code hosted [on github](https://github.com/dccouncil/donations)). It uses [django-tastypie](http://django-tastypie.readthedocs.org/) to create a simple API.

The API is found at [https://donationdisclosure.herokuapp.com/api/v1](https://donationdisclosure.herokuapp.com/api/v1)

### GET /donations

Returns a JSON response with the collection of all published donations made to the Council.

#### Examples

`https://donationdisclosure.herokuapp.com/api/v1/donations`

`https://donationdisclosure.herokuapp.com/api/v1/donations/1`

## License

The information and source code is in the public domain within the United States. Additionally, all copyright and related rights in the work worldwide are wavied through the CC0 1.0 Universal public domain dedication.
