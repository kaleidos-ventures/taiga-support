.. title: CSV Reports
.. slug: csv-reports
.. date: 2015-10-16 13:55:02 UTC+02:00
.. tags: 
.. category: Admin
.. order: 20
.. link: 
.. description: 
.. type: text

In Taiga you can make reports with some data and graph about your
projects. To do that you can use your favorite spreadsheet app and the
information about your user stories, tasks and issues in csv
(*comma-separated values*) format.

You can obtain the information like a csv file or like a csv data url,
one for user stories, other for tasks and other for issues.

Get a csv file:
===============

1. Go to *Admin > Project > Reports*.

   .. figure:: /resources/admin/csv-reports/csv_reports_step1.png
      :alt: CSV Reports - Step 1

      CSV Reports - Step 1

2. Click *Generate URL* link if url doesn’t exist yet.

   .. figure:: /resources/admin/csv-reports/csv_reports_step2.png
      :alt: CSV Reports - Step 2

      CSV Reports - Step 2

3. Click *Download CSV* buttton to start the download of the csv file.

…in Libre Office
================

1. Use the “Download csv” button and get a local copy of the file

2. Click *Insert > Sheet from file*

3. Enable the link option and click browse for selecting the downloaded
   file

   .. figure:: /resources/admin/csv-reports/libre_office_csv.png
      :alt: "Sheet from file" Panel

      "Sheet from file" Panel

Use csv data url…
=================

1. Go to *Admin > Project > Reports*.

2. Click *Generate URL* link if url doesn’t exist yet.

3. Copy the url (the icon on the right of the input is useful to select
   all text before press Ctrl+C).

…in Google Docs
===============

1. Create a new spreadsheet document.

2. Use the function `IMPORTDATA()`_ with the generated URL and press *ENTER*.

   .. figure:: /resources/admin/csv-reports/csv_export_1.png
      :alt: CSV Reports - Google Drive - Step 1

      CSV Reports - Google Drive - Step 1

3. The information will appear automatically.

   .. figure:: /resources/admin/csv-reports/csv_export_2.png
      :alt: CSV Reports - Google Drive - Step 2

      CSV Reports - Google Drive - Step 2

Remember that you can share the url and regenerate every time you want.
And a very important thing: **only the last generated url will be valid
for each type**.

.. _IMPORTDATA(): https://support.google.com/docs/answer/3093335
