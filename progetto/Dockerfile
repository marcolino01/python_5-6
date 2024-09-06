FROM python:3.10-alpine                
ADD myapp.py .
CMD [ "python","./myapp.py" ]
# FROM specifica l'immagine base da cui partire per crearne una nuova, in questo caso stiamo usando l'immagine python
# il tag 3.10-alpine specifica quali tra le diverse immagini python utilizzare
# ADD: è usato per copiare file o directory all'interno di una docker image. La sintassi prevede 2 parametri: ADD source destination source può essere un file oppure una URL.
# CMD: è usato per specificare quale comando deve eseguire il container quando viene lanciato