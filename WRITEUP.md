Hello,

I am still for of actually finishing this project, but I am bit stuck on both files, and feel I need some feedback to carry on.

Would appreciate if you can go through both python files and see if I am in the wrong direction.

Additionally I have some questions:
- I don't understand "load the model network into a self.net_plugin variable portion in loading the model
- What do I do with the request id in the asynchronous function, (I saw it in one of the exercises) 
- I am not sure how I can locate a non-trained model so I used one from openvino from now, would appreciate your guidance in searching for other alternatives. I used https://docs.openvinotoolkit.org/2019_R1/_person_detection_retail_0013_description_person_detection_retail_0013.html
- How do I calculate the duration? I think I am missing a key element

Thanks you!!

Second Submission:

I used https://docs.openvinotoolkit.org/2019_R1/person-detection-retail-0002.html

To convert the model:

cd /opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader

./downloader.py --name person-detection-retail-0002 -o /home/workspace

Source Framework is Caffee

python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model squeezenet_v1.1.caffemodel --input_proto deploy.prototxt

Alternative:

I found these models as recomended by one of my colleagues:https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md


wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar -xvf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz


python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config faster_rcnn_inception_v2_coco_2018_01_28/pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json








# Project Write-Up

You can use this document as a template for providing your project write-up. However, if you
have a different format you prefer, feel free to use it as long as you answer all required
questions.

## Explaining Custom Layers

The process behind converting custom layers involves...

Some of the potential reasons for handling custom layers are...

## Comparing Model Performance

My method(s) to compare models before and after conversion to Intermediate Representations
were...

The difference between model accuracy pre- and post-conversion was...

The size of the model pre- and post-conversion was...

The inference time of the model pre- and post-conversion was...

## Assess Model Use Cases

Some of the potential use cases of the people counter app are...

Each of these use cases would be useful because...

## Assess Effects on End User Needs

Lighting, model accuracy, and camera focal length/image size have different effects on a
deployed edge model. The potential effects of each of these are as follows...

## Model Research

[This heading is only required if a suitable model was not found after trying out at least three
different models. However, you may also use this heading to detail how you converted 
a successful model.]

In investigating potential people counter models, I tried each of the following three models:

- Model 1: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...
  
- Model 2: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...

- Model 3: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...
