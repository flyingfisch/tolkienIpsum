# tolkienIpsum

A Tolkien-themed lipsum generator built with Django

Teaching myself Django with this. Maybe it's overkill for this project, but you have to start somewhere!

If you want to try it out just make sure you have `python3` installed and do

~~~bash
$ git clone https://github.com/flyingfisch/tolkienIpsum/
$ cd tolkienIpsum
$ ./manage.py runserver
~~~

Then go to `http://localhost:8000/generator/10/5/15` in a browser and check it out!

## Directories

~~~
- generator -- the lipsum generator resides here
- node_modules -- just modules that grunt loads, not sure it is even necessary to keep in source control, but leaving it there to be safe
- static -- static files go here. In production these will be stored on a CDN
- tolkienIpsum -- where the urls, settings, and stuff are handled. Since this is my first django project, I'm not sure if the ui folder should be merged here as well. May do that sometime in the future.
- ui -- this is where the UI lives.
~~~



<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a>
<div>
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" property="dct:title" rel="dct:type">Tolkien Ipsum</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/flyingfisch/tolkienipsum" property="cc:attributionName" rel="cc:attributionURL">Mark Fischer, Jr.</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
</div>
