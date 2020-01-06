Please find the tutorial at https://medium.com/@samy_raps/flask-vue-mysql-on-docker-part-i-setting-up-320d55a85971

### Important commands

Create a folder called `data` inside the `db` folder.

Build and run :: `docker-compose up --build`

Build and run in the background and view logs for all the instances ::
`docker-compose up --build -d && docker-compose logs --tail=all -f`

Stop instances :: docker-compose down

Stop and Delete all containers :: `docker container stop $(docker container ls -aq) && docker container rm $(docker container ls -aq)`

_Cheers!_
