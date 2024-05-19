'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-05-19 17:00:11
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-05-19 17:00:28
FilePath: \Pytorch\Optimization.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scipy.optimize import minimize

def reprojection_error(params, image_points, point_cloud_points):
    # Extract parameters
    tx, ty, tz, rx, ry, rz = params
    
    # Construct the transformation matrix
    translation = np.array([tx, ty, tz])
    rotation_matrix = np.eye(3)  # Placeholder for rotation matrix computation
    
    transformed_points = (rotation_matrix @ point_cloud_points.T).T + translation
    
    error = np.linalg.norm(transformed_points - image_points, axis=1)
    return np.sum(error)

def optimize_transformation(image_points, point_cloud_points, initial_params):
    result = minimize(reprojection_error, initial_params, args=(image_points, point_cloud_points), method='BFGS')
    return result.x
