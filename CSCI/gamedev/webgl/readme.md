## overview

This project utilized a couple resources and the phenomenal three.js library to render a blender asset in the browser utilizing webgl. I utilized a web asset created previously, `snek`, for this implementation. A tutorial (https://threejs.org/docs/#manual/introduction/Creating-a-scene) was followed to setup the initial scene. Using the `Collada` exporter in `blender` and the `Collada` importer in `three.js` [1], the asset was successfuly loaded into the scene. The `snek` object was then rotated and ambient lighting was added to demonstrate how well the object was rendered. Further, the camera was given orbital control.


[1] : https://stackoverflow.com/questions/9783458/blender-export-to-three-js


## installation and usage

Please unpackage the zip file and open the index.html file in a browser through a web server. A web server must be used to load the file due to cross origin restrictions disabling the loading of the assets.

A simple webserver can be started by the following commands on a unix system:
```
npm install -g http-server
http-server .
```
