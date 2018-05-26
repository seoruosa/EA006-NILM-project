# EA006-NILM-project
Graduate final project

Container docker com nilmtk instalada
https://hub.docker.com/r/skipeco/nilmtk1/

###Comandos###
**Baixar o docker**
`docker pull skipeco/nilmtk1`

**Subir docker e abrir um Jupyter notebook no http://localhost:8888/tree**
`docker run -p 8888:8888 -it -v ~/TCC/nilmtk/data:/nilmtk/data skipeco/nilmtk1 /bin/sh -c "cd nilmtk; jupyter notebook"`

**Subir docker e abrir bash**
`docker run -i -t -v ~/TCC/nilmtk/data:/nilmtk/data skipeco/nilmtk1 /bin/bash`

**Subir docker, abrir Jupyter notebook e bash**
`docker run -p 8888:8888 -it -v ~/TCC/nilmtk/data:/nilmtk/data skipeco/nilmtk1 /bin/sh -c "cd nilmtk; jupyter notebook & /bin/bash"`

`docker ps`
`docker start <container>`

