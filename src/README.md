# Masdap

## Localhost Dev Deployment

```
python create-envfile.py -hn localhost --email alessio.fabiani@geosolutionsgroup.com --geonodepwd admin --geoserverpwd geoserver --pgpwd postgres --dbpwd geonode --geodbpwd geonode --clientid 12345 --clientsecret 6789012345 --secret_key 01234567890 --env_type dev

docker-compose build
docker-compose up
```
