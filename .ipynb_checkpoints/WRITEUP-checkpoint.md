
# Project Write-Up

You can use this document as a template for providing your project write-up. However, if you
have a different format you prefer, feel free to use it as long as you answer all required
questions.

## Explaining Custom Layers

The process behind converting custom layers involves adding layers that are not part of any known layers.
The model extraction extracts the informartion from an input. THe output is then handeled using model optimization based on a certain shape for the output. Finally, the xml and bin files are created as part of the IR output. whihc is needed by the inference Engine to run the model.

Some of the potential reasons for handling custom layers is to add extensions to both the Model Optimizer and the Inference Engine

## Comparing Model Performance

I am using three models in this comparison:

- faster_rcnn_inception_v2
- ssd_mobilenet_v2_coco
- ssd_mobilenet_v2_quantized_coco

[This link](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) has more info about these models.

To convert the following models the following commands are used:

Download and untar the files on the local directory. Then run the below commands



```
#faster_rcnn_inception_v2
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar -xvf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
cd faster_rcnn_inception_v2_coco_2018_01_28
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json

#ssd_mobilenet_v2_coco
wget http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2018_01_28.tar.gz
tar -xvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz 
cd ssd_mobilenet_v2_coco_2018_03_29
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_support.json

#ssd_mobilenet_v1_coco
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz

tar -xvf ssd_mobilenet_v1_coco_2018_01_28.tar.gz
cd ssd_mobilenet_v1_coco_2018_01_28
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_support.json
```


A simple comparison between the models are the following:

| Model            | Speed (ms) | Ex Time (s) | File Size (Mb) |
|------------------|------------|-------------|----------------|
| faster_rcnn      | 58         | 143         | 53             |
| ssd_mobilenet_v2 | 31         | 57          | 67             |
| sd_mobilenet_v1  | 30         | 39          | 27             |



I will be using the ssd_mobilenet_v2 model since due to its effectivenss and due to several recomendations

## Assess Model Use Cases

The use case for a people counter app could be useful in several cases. 
- You could generall count the people that are in a building. This could potentially help in limiting the number of people in a certain area, especially during the current convid situation
- You can gather metrics about certain behaviour or habits of people visiting a certain location (a mall or a workplace). Accordingly you wouild be able make some rearrangment to provide the best user experience.
- You can gather insights about people engagement for certain topics compared to others in conferneces. That way, you would be able to poinpoint the general interests of the public and thus direct research and projects towards that.




## Assess Effects on End User Needs

Lighting, model accuracy, and camera focal length/image size have different effects on a
deployed edge model. The potential effects of each of these are as follows:

- the lighting can influence the edge model on counting the people in frame. With certain angles the model can mistakenly ignore a person in the frame (or give it a lower confidence level) due to missing charectersitcs 
- The image size can infuence the overall processing. If the image size is too large, the edge compute might need more time to process the frame and thus exhaust mroe resources. A lower sized image can influence the accuracy of the output and thus jeopardize the project
- model accuracy is proportional to compute power and memory consumption. The higher the model accuracy, the more resoureces it would potentially need. I believe this is more dependant on the use case. If a high accuracy is a must, then using more computational power should be tolerated. In a more relaxed enviroment without need for precision, it is acceptable aim for a lower accuracy to save on resources for other applications.



## Running the project
To run the application run the follwoing after running the MQTT server in other terminals:


```
#1st terminal
cd webservice/server/node-server
node ./server.js

#2nd terminal
cd webservice/ui
npm run dev

#3rd terminal
sudo ffserver -f ./ffmpeg/server.conf

#4th terminal
source /opt/intel/openvino/bin/setupvars.sh -py


python main.py -i resources/Pedestrian_Detect_2_1_1.mp4 -m frozen_inference_graph.xml -l /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so -d CPU -pt 0.7 | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm

(I am getting some errors, and not sure how to carry on)



