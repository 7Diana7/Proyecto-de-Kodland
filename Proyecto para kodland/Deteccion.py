from imageai.Detection import ObjectDetection

def detect_objects_on_road(input_image, model_path):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    detections = detector.detectObjectsFromImage(
        input_image=input_image,
        output_image_path="output_image.jpg",
        minimum_percentage_probability=30)

    return detections