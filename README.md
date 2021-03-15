# CMSC447-IndivAssignment

To run the program:


Download files


Create a react app in the same folder you have the 'flask api' folder


Replace the SRC and package.json files in the react app


Go into flask-api and start the virtual environment

Type 'python init_db.py' to initialize the database

then type 'flask run' to start the program

From there, go to the react app and type 'yarn start'


You now have both servers running


navigate to http://localhost:3000 to view the react client side. I was able to get react to read from flask, but I could not get it to write. You can delete students from this menu, but it directs you to http://127.0.0.1:5000, which is the flask backend and does not go through react.


However, this client is totally functional in CRUD abilities.


