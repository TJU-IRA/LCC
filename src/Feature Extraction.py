import cv2
import numpy as np
import open3d as o3d

def extract_features_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Detect the circular board
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=100, param2=30, minRadius=50, maxRadius=150)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            return (x, y), r
    else:
        raise ValueError("No circles detected")

def extract_features_from_point_cloud(point_cloud_path):
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(point_cloud_path)
    
    # Fit a plane to the point cloud to find the normal
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
    
    [a, b, c, d] = plane_model
    normal = np.array([a, b, c])
    
    # Compute the centroid of the inliers (points on the plane)
    inlier_cloud = pcd.select_by_index(inliers)
    centroid = np.mean(np.asarray(inlier_cloud.points), axis=0)
    
    return centroid, normal
