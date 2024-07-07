# nonlocal-munchkin

## MUNCHKIN (112 EDITION)

Munchkin is a popular turn-based card game. My project remakes munchkin into "Munchkin: 112 Edition". There are two versions of the game: a machine-local version and a PVP multiplayer version. The machine-local version allows you to play with other humans and AI but the game display system is a bit different than a real game of munchkin. The local multiplayer version allows you to both play locally and with other friends non-locally as long as they have your external IP address and is more akin to how the game would be played in real life.

## Running

In order to run the machine-local version of the game, simply run the  munchkin_client.py file and begin playing.

In order to run the non-local multiplayer version of the game. Be sure to assign your external IP address to the variable named 'HOST' in both the munchkin_server.py and munchkin_client.py files and then assign the variable 'PORT' to a forwarded port. Note that if you do not have access to a forwarded port, you can play the game with multiple players on a single machine by utilizing a port above 50000 and assigning 'HOST' to your local IP address.

Before any players can join the game, make sure to run the munchkin_server.py file on the server machine and then players can join by running the munchkin_client.py file on their respective machines.

## Libraries

Make sure that your machine is running Python3 (sockets and threading libraries will already be included). The only aditional module required is Pygame 1.9.6 which can be found here:https://www.pygame.org/download.shtml

## Shortcuts

There are no shortcuts in the game - as this is a turn based card game and there is no need to skip from one portion of the game to another. That being said, however, one can increase or decrease the time it takes for an AI to move by increasing or decreasing (respectively) the self.interval class attribute in the munchkin_main.py file.

## Links

Visit this link for a demo about the features in this project: [Demo Video](https://youtu.be/-7MqCEfxmR4)
