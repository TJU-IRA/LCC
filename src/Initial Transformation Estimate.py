'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-05-19 16:59:38
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-05-19 16:59:45
FilePath: \Pytorch\Initial Transformation Estimate.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def compute_initial_transformation(image_features, point_cloud_features):
    image_centroid, image_radius = image_features
    point_cloud_centroid, point_cloud_normal = point_cloud_features
    
    # Assume some initial alignment based on the centroids and the normal vectors
    translation = point_cloud_centroid - np.array([image_centroid[0], image_centroid[1], 0])
    
    # For rotation, assume the normal vectors should align (simple case)
    # More complex approaches would involve computing the full rotation matrix
    normal_alignment = point_cloud_normal
    
    return translation, normal_alignment
