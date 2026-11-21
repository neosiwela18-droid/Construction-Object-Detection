# Construction-Object-Detection

## All classes:

1. boots	

2. construction_vest	

3. fork_lift	

4. gloves	

5. goggles	

6. helmet	

7. no_boots	

8. no_construction_vest	

9. no_gloves	

10. no_goggles	

11. no_helmet

12. person


### Example Use Case of Image Object Detection and Localization:
---
## The Original Image shows a men in construction gear:

<img width="714" height="893" alt="image" src="https://github.com/user-attachments/assets/e58b44d0-59d6-473a-b3b1-90f1ae3faf3e" />


## Detected Elements & Confidence Scores

The colored bounding boxes show what the AI identifies along with its confidence percentage:

### Compliant Gear:

	• Helmet (92.92%): Detects the orange hard hat on the worker's head.
	
	• Construction Vest (90.30% & 47.77%): Identifies the high-visibility orange and reflective gear on his torso, with a second, lower-confidence detection on his pant leg due to the matching orange color.
	
	• Boots (84.59% & 87.83%): Confirms he is wearing protective footwear.
	
  • Person: Identifies a person with the purple bounding box.
  
## Missing Gear (Safety Violations):

	• No Goggles (71.03%): Flags that his eyes are unprotected near active drilling machinery and splashing debris.
	
	• No Gloves (76.45% & 79.15%): Flags both of his bare hands as exposed to pinch points, heavy equipment, and rough materials.
  
<img width="356" height="443" alt="image" src="https://github.com/user-attachments/assets/488f897b-66f7-4e97-89db-46e9735d4fe9" />
