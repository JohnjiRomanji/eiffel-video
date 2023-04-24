import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import csv

# Load the model from TensorFlow Hub
model = hub.KerasLayer('https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_europe_V1/1', output_key="predictions:logits")


filename = f"eiffel_posts_good.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Image URL", "Post Permalink", "Post URL"])

j=0
i=1
number = 0
with open("eiffel_posts.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    with open("progress.txt", "r") as file:
            number = int(file.read())
            print(number)
    for l in range(number): 
        next(reader)
    for row in reader: 
        try:
            image_url = row[0]
            # Load and preprocess the input image
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            if img.mode in ("RGBA", "LA"):
                # Remove alpha channel by converting to RGB mode
                img = img.convert("RGB")
            img = img.resize((321, 321)) # The input shape expected by the model
            img = np.array(img).astype(np.float32)
            img = (img - 127.5) / 127.5 # Normalize to [-1, 1]
            img = np.expand_dims(img, axis=0) # Add batch dimension

            
            logits = model(img)
            # Get the top 5 predictions
            top_k = 5
            indices = tf.argsort(logits, direction="DESCENDING")[0][:top_k]
            scores = tf.gather(logits[0], indices)
            
            best=indices.numpy()

            names=[]
            with open('map.csv', 'r') as f:
                reader = csv.reader(f)
                for row2 in reader:
                    for id in best:
                        if str(id) in row2[0]:
                            # Do something with the row that contains the specific value
                            names.append(row2[1])
            top_5 = names[:5]
            print(f"Detected {top_5} at {scores[0].numpy()*100}%")
            if "Eiffel Tower" in top_5: 
                filename = f"eiffel_posts_good.csv"
                with open(filename, "a+", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    repeat = False
                    with open(filename, 'r') as f:
                        reader = csv.reader(f)
                        for row3 in reader:
                            if str(i) in row3[0]: 
                                repeat = True
                        if not repeat: 
                            writer.writerow([str(i)]+row)
                            print([str(i)]+row)
                i+=1
            j+=1
            with open("progress.txt", "w") as file:
                file.write(str(number+j))
            print(number+j)
        except:
            pass


#28796 is the Eiffel Tower

#predicted_label = label_map[np.argmax(predictions)]
#print("Predicted label:", predicted_label)

#print(result.keys())