terminal:
# install docker image

- docker run get_data

# up docker-compose with postgresql

- docker-compose up -d --build

# for start parse and add to database objects, run ->

- python3 ./get_data.py 

# for print result ->

- python3 ./print_data.py 