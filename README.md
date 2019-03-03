Copy env.template to env and set a secure password

Command to create loaddata.json:

    python manage.py dumpdata --natural-primary --natural-foreign > loaddata.json
    
Flow to update plugins once in production.
 1) Freeze content in prod (tell users they can't make changes until the change is done)
 2) Dump the prod database
 3) Use this dump to do local development
 4) Create a new loaddata.json after dev is complete (probably good idea to archive and date old .json)
 5) Deploy the app with new loaddata.json to prod
