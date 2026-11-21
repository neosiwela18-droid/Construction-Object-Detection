import cv2 as cv
from inference_sdk import InferenceConfiguration, InferenceHTTPClient



client = InferenceHTTPClient(
                            api_key=API_KEY,
                            api_url=API_URL
).configure(InferenceConfiguration(
                                    api_key_transport='header'
                                    ))
                            
result = client.run_workflow(
                            workspace_name=WORKSPACE_NAME,
                            workflow_id= WORKFLOW_ID,
                            images= {'image': IMAGE_PATH},
                            use_cache= True
)

predict = result[0]['predictions']['predictions']

frame = cv.imread(IMAGE_PATH)

CLASS_COLOURS =     {
                    "person": (255, 89, 94),
                    "construction_vest": (0, 200, 255),
                    "helmet": (255, 200, 0),
                    "boots": (0, 255, 127),
                    "no_gloves": (0, 0, 255),
                    "goggles": (0, 255, 255),
                    "no_goggles": (255, 0, 255),
                    }


def bounding_box(frame, x, y, w, h, label, conf, colour):
    x1 = int(x - w / 2) # Left Side
    y1 = int(y - h / 2) # Top Side
    x2 = int(x + w / 2) # Right Side
    y2 = int(y + h / 2) # Bottom Side
        
    
    h_img, w_img = frame.shape[:2]
    x1, y1 = max(0, x1), max(0, y1) #Never goes beyon (0,0)
    x2, y2 = min(w_img - 1, x2), min(h_img - 1, y2) #Never goes beyond frame.shape[:2]

    
    cv.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    colour,
                    2
                    )


    text = f'{label} {100 * conf:.2f}%'
    (tw, th), baseline = cv.getTextSize(
                                        text, 
                                        cv.FONT_HERSHEY_SIMPLEX,
                                        0.55,
                                        1, 
                                        )
    
    
    ty = y1 - 8
    if ty - th < 0:
        ty = y1 + th + 8
        
    cv.rectangle(
                    frame, 
                    (x1, ty - th - 5),
                    (x1 + tw + 6, ty + 5),
                    colour,
                    -1,
                    )
    
    cv.putText(frame,
               text, 
               (x1 + 3, ty),
               cv.FONT_HERSHEY_SIMPLEX,
               0.55,
               (0, 0, 0),
               1,
               cv.LINE_AA,
               )
    
    cv.imwrite('Model_outcome.jpg', frame)
    return frame
    
    
for pred in predict:
    clss = pred['class']
    color = CLASS_COLOURS.get(clss, (255, 255, 255))
    
    frame = bounding_box(
        frame,
        pred['x'],
        pred['y'],
        pred['width'],
        pred['height'],
        clss,
        pred['confidence'],
        color,
    )
    
cv.imshow('', frame)
cv.waitKey(0)
