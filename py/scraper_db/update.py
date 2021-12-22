import pathlib
import requests
import os
import hashlib
import config
from PIL import Image

def addYear(cnx,year,album_id):

    add_year = (
        "UPDATE album "
        "SET year = %(year)s "
        "WHERE id = %(id)s"
    )

    cursor = cnx.cursor()

    cursor.execute(add_year,{
        'year' : year,
        'id' : album_id
    })

    cnx.commit()
    cursor.close()

    if cursor.rowcount == 0:
        return False
    else:
        print("id",album_id,"added year")
        return True

def addImage(cnx,url,album_id):
    # create temp directory
    pathlib.Path(config.temp_image_path).mkdir(parents=True, exist_ok=True)
    # create temp file name
    temp_filename = url.split("/")[-1]

    # download image to temp location
    r = requests.get(url, stream = True)
    if r.status_code == 200:
        with open(config.temp_image_path + temp_filename,"wb") as file:
            for chunk in r:
                 if chunk:
                     file.write(chunk)

        # hash primary key
        h = hashlib.new("md5")
        h.update(str(album_id).encode())
        hash = h.hexdigest()

        # create new path and filename
        new_path = hash[0:2] + "/" + hash[3:5] + "/"
        new_filename = hash[6:]
        filetype = pathlib.Path(config.temp_image_path+temp_filename).suffix

        # create path
        pathlib.Path(config.image_path + new_path).mkdir(parents=True, exist_ok=True)

        # move file
        os.rename(config.temp_image_path + temp_filename,config.image_path + new_path + new_filename + filetype)

        # insert image location into db
        add_image = (
            "UPDATE album "
            "SET image = %(image)s "
            "WHERE id = %(id)s"
        )

        cursor = cnx.cursor()

        cursor.execute(add_image,{
            'image' : new_path + new_filename + filetype,
            'id' : album_id
        })

        cnx.commit()
        cursor.close()

        if cursor.rowcount == 0:
            return False
        else:
            print("id",album_id,"added cover")
            return True

def resizeImage(cnx,id,image):

    def resize(infile):
        with Image.open(infile) as im:
            (width, height) = (250,250)
            im_resized = im.resize((width, height))
            im_resized.save(infile)

    def setResizedTrue(cnx,album_id):
        # create sql statement
        image_resized = (
        "UPDATE album "
        "SET resized = TRUE "
        "WHERE id = (%s)"
        )

        # create cursor
        cursor = cnx.cursor()

        # run statment
        cursor.execute(image_resized,(album_id,))

        # commit and close
        cnx.commit()
        cursor.close()

    resize(config.image_path + image)
    setResizedTrue(cnx,id)
