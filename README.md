# Eiffel Video
 
The final product can be found on [Youtube](https://youtube.com)

Create a video of a fast sequence of aligned images of the Eiffel tower. Using Googles landmark Recogniftion Model (fine-tuned for Europe) on [Tensorflow hub](https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_europe_V1/1), filter thoruigh images scraped from Reddit using PRAW, picking only the ones with Eiffel Tower in the top 5 detected outputs. 

Using the 165 filtered images edit manually in shotcut to adjust position, add music. 

Image posts/links in eiffel_posts_good.csv, not all posts are guaranteed to be used in the final video. 

Music: [Know you Miss Me - Chasinbens](https://youtu.be/d8KKO_i3Xo4)

Landmarks Model: 
Cao B, Araujo A, Sim J. Unifying Deep Local and Global Features for Image Search. arXiv 2020. Available: https://arxiv.org/abs/2001.05027
Weyand T, Araujo A, Cao B, Sim J. Google Landmarks Dataset v2-A Large-Scale Benchmark for Instance-Level Recognition and Retrieval. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020. Available: https://arxiv.org/abs/2004.01804