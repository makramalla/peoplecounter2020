Hello,

I am still not clear on how to search for untrained models.

I found these models that one of my colleagues used:
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
Not sure if this is correct or not but i will use it to carry on.

Important note: I found this model on the following github repo:
https://github.com/prateeksawhney97/People-Counter-Application-Using-Intel-OpenVINO-Toolkit
I can safely assume that this is a project submission as well. I did not try to copy or recreate any of my colleagues efforts, which I believe is clear in my submission. 


wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar -xvf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz


python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config faster_rcnn_inception_v2_coco_2018_01_28/pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json


Which brings me to the next question, how do I compare models?
Does this happen before or after the processing.
What are my metrics and how to obtain them?


I have updated the main and inferense python based on the previous recommendation. (Thank you)

Running the code (after running three other terminals) gets the following error:

(venv) root@d73d0c526396:/home/workspace# python main.py -i resources/Pedestrian_Detect_2_1_1.mp4 -m frozen_inference_graph.xml -l /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so -d CPU -pt 0.7 | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 1280x720 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
[rawvideo @ 0x1b40d80] Invalid buffer size, packet size 130 < expected frame_size 2764800
Error while decoding stream #0:0: Invalid argument
Output file is empty, nothing was encoded (check -ss / -t / -frames parameters if used)


Further recommendations would be really appreciated
Thanks








The next section will be finalized when i am more confident about my submission.


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
