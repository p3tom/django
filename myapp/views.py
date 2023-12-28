from django.shortcuts import render
from django.db import connection

def sensor_list(request):
    with connection.cursor() as cursor:
       cursor.execute("SELECT * FROM aqs.sensor;")
       data = cursor.fetchall()
       print("SQL Query:", cursor.query)

    columns = [col[0] for col in cursor.description] if data else []

    return render(request, './sensor_list.html', {'data': data, 'columns': columns})


# def sensor_detail(request, sensor_id):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM sensor WHERE id = %s;", [sensor_id])
#         sensor = cursor.fetchone()

#     return render(request, 'myapp/sensor_detail.html', {'sensor': sensor})
# pass