import csv
from fastapi.responses import StreamingResponse
import laspy
import numpy as np


las_data = 'data/Sydney_fig_tree.laz'

def read_pointCloud():
    las =laspy.open(las_data,'r')
    return las

def read_pointCloud_count():
    return read_pointCloud().header.point_count

def read_pointCloud_format():
    point_format = read_pointCloud().header.point_format
    return point_format.id

def read_pointCloud_dimension_names():
    print(list(read_pointCloud_format().dimension_names))
    return list(read_pointCloud_format().dimension_names)


def read_pointCloud_xyz(point_number:int):
    las_file = read_pointCloud()
    dataset=[]    
    for points in las_file.chunk_iterator(point_number):
        dataset = np.vstack((points.x,points.y,points.z)).transpose()
    return dataset
    
if __name__ == '__main__':
    read_pointCloud_count()
    read_pointCloud_format
    read_pointCloud_dimension_names()
    read_pointCloud_xyz()
