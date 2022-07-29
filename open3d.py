import open3d as o3d
import numpy as np


if __name__ == "__main__":
    print("Loading Point Cloud")
    ptCloud = o3d.io.read_point_cloud('./busako_printed.ply')
    
    print(ptCloud)
    print(np.asarray(ptCloud.points))
    
    o3d.visualization.draw_geometries([ptCloud])
    
    o3d.io.write_point_cloud("output.ply", ptCloud)
    
    

