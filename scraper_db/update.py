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
